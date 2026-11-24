"""Mede a tinta dos manuscritos por família de cor: preto, azul, verde, vermelho e outra.

As cores dos manuscritos são famílias de tom, não valores exatos. Um pixel com
pouca cor (croma baixo) é tinta preta, seja qual for o brilho: o traço leve,
que parece cinza, também é preto. Um pixel com cor é classificado pelo matiz:
azul, verde, vermelho ou outra (que pede confirmação do usuário). O papel é o pixel sem
cor e claro.

Uso, a partir da raiz do repositório (a .venv é ignorada pelo git):

    py -V:3.13 -m venv .venv
    .venv\\Scripts\\python -m pip install -r .agents/skills/consolidar-exercicio/ferramentas/requirements.txt
    .venv\\Scripts\\python .agents/skills/consolidar-exercicio/ferramentas/tinta.py <comando> ...

Comandos:

    inventario <pasta>            lista as imagens da pasta (com subpastas, como
                                  Restos/), a fração de tinta de cada família e as
                                  possíveis versões: imagens cuja tinta está contida
                                  na de outra, como uma página fotografada antes de
                                  ser continuada.
    faixas <imagem|pasta>...      divide cada imagem em faixas horizontais (linhas
                                  de texto) e diz as famílias de cada faixa e onde
                                  cada uma está na largura; marca as faixas mistas,
                                  como uma nota azul na margem de um texto preto.
    camadas <imagem|pasta>...     grava, para cada família presente, uma imagem só
                                  com a tinta dela, em <pasta da imagem>/.camadas/
                                  ou em --saida.

A saída é Markdown, pronta para o mapa de cobertura. A ferramenta orienta a
leitura; quem decide é a imagem.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps

# Códigos devolvidos por classificar().
FUNDO, PRETO, AZUL, VERDE, OUTRA = range(5)
VERMELHO = 5  # preserva os códigos das famílias existentes
NOMES = {PRETO: "preto", AZUL: "azul", VERDE: "verde", VERMELHO: "vermelho", OUTRA: "outra"}

# Limiares, calibrados nas páginas do Exercício 1.1 do Curso de Análise.
CROMA_MIN = 35  # max(R,G,B) − min(R,G,B) a partir do qual o pixel tem cor
BRILHO_FUNDO = 215  # pixel sem cor com max(R,G,B) a partir disso é papel
AZUL_MATIZ = (180.0, 290.0)  # graus, intervalo semiaberto
VERDE_MATIZ = (70.0, 180.0)
VERMELHO_MATIZ = (330.0, 25.0)  # [330, 360) ou [0, 25): atravessa o zero
PRESENCA_MIN = 0.005  # fração da tinta abaixo da qual uma família é ruído
MISTO_MIN = 0.10  # fração da segunda família que torna uma faixa mista
CONTENCAO_MIN = 0.90  # fração da tinta de uma imagem dentro da de outra
GRADE_COLUNAS = 160  # colunas da grade que compara imagens
TINTA_MIN_FAIXA = 50  # pixels de tinta abaixo dos quais a faixa é ruído
LINHA_TINTA_MIN = 0.008  # fração da largura com tinta para a linha de pixels contar
FOLGA_DIVISOR = 300  # linhas vazias até altura/FOLGA_DIVISOR não separam faixas

EXTENSOES = {".png", ".jpg", ".jpeg", ".webp"}


def carregar(caminho: Path, reducao: int = 1) -> np.ndarray:
    """Abre a imagem como RGB sobre fundo branco, já na orientação do EXIF."""
    img = ImageOps.exif_transpose(Image.open(caminho))
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        rgba = img.convert("RGBA")
        fundo = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
        fundo.alpha_composite(rgba)
        img = fundo
    img = img.convert("RGB")
    if reducao > 1:
        img = img.reduce(reducao)
    return np.asarray(img)


def classificar(rgb: np.ndarray) -> np.ndarray:
    """Rotula cada pixel: FUNDO, PRETO, AZUL, VERDE, VERMELHO ou OUTRA."""
    px = rgb.astype(np.int16)
    maximo = px.max(axis=-1)
    croma = maximo - px.min(axis=-1)
    rotulos = np.zeros(maximo.shape, dtype=np.uint8)
    colorido = croma >= CROMA_MIN
    rotulos[~colorido & (maximo < BRILHO_FUNDO)] = PRETO
    if colorido.any():
        r, g, b = (px[..., i][colorido] for i in range(3))
        m = maximo[colorido]
        c = croma[colorido].astype(np.float32)
        matiz = 60.0 * np.where(
            m == r,
            ((g - b) / c) % 6.0,
            np.where(m == g, (b - r) / c + 2.0, (r - g) / c + 4.0),
        )
        familia = np.full(matiz.shape, OUTRA, dtype=np.uint8)
        familia[(matiz >= VERDE_MATIZ[0]) & (matiz < VERDE_MATIZ[1])] = VERDE
        familia[(matiz >= AZUL_MATIZ[0]) & (matiz < AZUL_MATIZ[1])] = AZUL
        familia[(matiz >= VERMELHO_MATIZ[0]) | (matiz < VERMELHO_MATIZ[1])] = VERMELHO
        rotulos[colorido] = familia
    return rotulos


def contar(rotulos: np.ndarray) -> dict[int, int]:
    """Pixels de cada família de tinta."""
    contagens = np.bincount(rotulos.ravel(), minlength=len(NOMES) + 1)
    return {familia: int(contagens[familia]) for familia in NOMES}


def presentes(contagens: dict[int, int]) -> list[tuple[int, float]]:
    """Famílias acima do ruído, com sua fração da tinta, da maior para a menor."""
    total = sum(contagens.values())
    if total == 0:
        return []
    fracoes = [(f, n / total) for f, n in contagens.items() if n / total >= PRESENCA_MIN]
    return sorted(fracoes, key=lambda par: -par[1])


def descrever(contagens: dict[int, int]) -> str:
    fracoes = presentes(contagens)
    if not fracoes:
        return "sem tinta"
    return " · ".join(f"{NOMES[f]} {round(100 * p)}%" for f, p in fracoes)


def grade(rotulos: np.ndarray) -> np.ndarray:
    """Reduz a tinta a uma grade grossa de células, marcadas se têm tinta."""
    tinta = rotulos != FUNDO
    altura, largura = tinta.shape
    celula = max(1, largura // GRADE_COLUNAS)
    linhas, colunas = altura // celula, largura // celula
    recorte = tinta[: linhas * celula, : colunas * celula]
    return recorte.reshape(linhas, celula, colunas, celula).any(axis=(1, 3))


def contencao(a: np.ndarray, b: np.ndarray) -> float:
    """Fração das células com tinta de a que também têm tinta em b."""
    if a.shape != b.shape or not a.any():
        return 0.0
    return float((a & b).sum() / a.sum())


@dataclass
class Faixa:
    y0: int
    y1: int
    contagens: dict[int, int]
    alcance: dict[int, tuple[float, float]] = field(default_factory=dict)

    def mista(self) -> bool:
        fracoes = presentes(self.contagens)
        return len(fracoes) > 1 and fracoes[1][1] >= MISTO_MIN


def faixas(rotulos: np.ndarray, folga: int | None = None) -> list[Faixa]:
    """Agrupa as linhas de pixels com tinta em faixas horizontais.

    O limiar por linha de pixels impede que um traço fino e vertical, como o que
    separa uma nota de margem, emende todas as linhas de texto numa faixa só.
    """
    tinta = rotulos != FUNDO
    altura, largura = tinta.shape
    limiar = max(2, int(largura * LINHA_TINTA_MIN))
    folga = folga if folga is not None else max(3, altura // FOLGA_DIVISOR)
    intervalos: list[tuple[int, int]] = []
    inicio = ultimo = None
    for y in np.flatnonzero(tinta.sum(axis=1) >= limiar):
        if inicio is None:
            inicio = ultimo = int(y)
        elif y - ultimo <= folga:
            ultimo = int(y)
        else:
            intervalos.append((inicio, ultimo))
            inicio = ultimo = int(y)
    if inicio is not None:
        intervalos.append((inicio, ultimo))

    resultado = []
    for y0, y1 in intervalos:
        trecho = rotulos[y0 : y1 + 1]
        contagens = contar(trecho)
        if sum(contagens.values()) < TINTA_MIN_FAIXA:
            continue
        faixa = Faixa(y0, y1, contagens)
        for familia, _ in presentes(contagens):
            colunas = np.flatnonzero((trecho == familia).any(axis=0))
            x0, x1 = np.quantile(colunas, [0.01, 0.99])
            faixa.alcance[familia] = (100 * x0 / largura, 100 * x1 / largura)
        resultado.append(faixa)
    return resultado


def chave_natural(caminho: Path) -> tuple:
    """Ordena 6, 6.1, 6.2, 6.10, 7, e números antes de nomes de subpastas."""
    # A extensão não deve fazer 6.1.png preceder 6.png. O nome completo
    # desempata formatos diferentes da mesma identificação numérica.
    partes = re.split(r"(\d+)", caminho.with_suffix("").as_posix().lower())
    natural = tuple((0, int(p)) if p.isdigit() else (1, p) for p in partes if p)
    return natural, caminho.as_posix().lower()


def listar_imagens(alvo: Path) -> list[Path]:
    """Imagens de um arquivo ou pasta, sem as pastas ocultas (como .camadas)."""
    if alvo.is_file():
        return [alvo]
    imagens = [
        p
        for p in alvo.rglob("*")
        if p.suffix.lower() in EXTENSOES
        and not any(parte.startswith(".") for parte in p.relative_to(alvo).parts)
    ]
    return sorted(imagens, key=lambda p: chave_natural(p.relative_to(alvo)))


def porcento(x: float) -> str:
    return f"{x:.1f}%".replace(".", ",")


def decimal(x: float) -> str:
    return f"{x:.2f}".replace(".", ",")


def cmd_inventario(pasta: Path, reducao: int) -> None:
    imagens = listar_imagens(pasta)
    if not imagens:
        print(f"Nenhuma imagem em {pasta}.")
        return
    print(f"## Inventário — {pasta.as_posix()}\n")
    print("| imagem | tamanho | tinta | famílias |")
    print("|---|---|---|---|")
    grades: dict[str, np.ndarray] = {}
    outras: list[str] = []
    for caminho in imagens:
        nome = caminho.relative_to(pasta).as_posix()
        with Image.open(caminho) as img:
            largura, altura = ImageOps.exif_transpose(img).size
        rotulos = classificar(carregar(caminho, reducao))
        contagens = contar(rotulos)
        fracao_tinta = sum(contagens.values()) / rotulos.size
        print(f"| {nome} | {largura}×{altura} | {porcento(100 * fracao_tinta)} | {descrever(contagens)} |")
        grades[nome] = grade(rotulos)
        if any(f == OUTRA for f, _ in presentes(contagens)):
            outras.append(nome)

    versoes = []
    nomes = list(grades)
    for i, a in enumerate(nomes):
        for b in nomes[i + 1 :]:
            ab, ba = contencao(grades[a], grades[b]), contencao(grades[b], grades[a])
            if ab >= CONTENCAO_MIN and ba >= CONTENCAO_MIN:
                versoes.append(f"- {a} e {b} são quase idênticas (contenção {decimal(ab)} e {decimal(ba)}).")
            elif ab >= CONTENCAO_MIN:
                versoes.append(f"- {a} está contida em {b} (contenção {decimal(ab)}): pode ser uma versão anterior.")
            elif ba >= CONTENCAO_MIN:
                versoes.append(f"- {b} está contida em {a} (contenção {decimal(ba)}): pode ser uma versão anterior.")
    print("\n**Possíveis versões:**" + (" nenhuma." if not versoes else "\n"))
    for linha in versoes:
        print(linha)
    if outras:
        print(
            "\n**Atenção:** tinta fora das famílias preta, azul, verde e vermelha em "
            + ", ".join(outras)
            + ". Confira na imagem e pergunte ao usuário o papel dessa cor."
        )


def cmd_faixas(alvos: list[Path], reducao: int) -> None:
    for alvo in alvos:
        for caminho in listar_imagens(alvo):
            rotulos = classificar(carregar(caminho, reducao))
            altura = rotulos.shape[0]
            print(f"### {caminho.as_posix()}\n")
            print("| faixa | y (px) | y (%) | famílias | alcance na largura (%) |")
            print("|---|---|---|---|---|")
            for n, faixa in enumerate(faixas(rotulos), start=1):
                y_px = f"{faixa.y0 * reducao}–{(faixa.y1 + 1) * reducao}"
                y_pc = f"{round(100 * faixa.y0 / altura)}–{round(100 * (faixa.y1 + 1) / altura)}"
                familias = descrever(faixa.contagens) + (" **misto**" if faixa.mista() else "")
                alcance = " · ".join(
                    f"{NOMES[f]} {round(x0)}–{round(x1)}" for f, (x0, x1) in faixa.alcance.items()
                )
                print(f"| {n} | {y_px} | {y_pc} | {familias} | {alcance} |")
            print()


def cmd_camadas(alvos: list[Path], saida: Path | None, reducao: int) -> None:
    for alvo in alvos:
        for caminho in listar_imagens(alvo):
            rgb = carregar(caminho, reducao)
            rotulos = classificar(rgb)
            destino_pasta = saida or caminho.parent / ".camadas"
            destino_pasta.mkdir(parents=True, exist_ok=True)
            for familia, _ in presentes(contar(rotulos)):
                mascara = rotulos == familia
                camada = np.full_like(rgb, 255)
                camada[mascara] = rgb[mascara]
                destino = destino_pasta / f"{caminho.stem}.{NOMES[familia]}.png"
                Image.fromarray(camada).save(destino, optimize=True)
                print(destino.as_posix())


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description="Mede a tinta dos manuscritos por família de cor (preto, azul, verde, vermelho)."
    )
    comandos = parser.add_subparsers(dest="comando", required=True)

    inventario = comandos.add_parser("inventario", help="famílias por imagem e possíveis versões")
    inventario.add_argument("pasta", type=Path)
    inventario.add_argument("--reducao", type=int, default=2, help="fator de redução (padrão 2)")

    por_faixa = comandos.add_parser("faixas", help="famílias por faixa horizontal")
    por_faixa.add_argument("alvos", nargs="+", type=Path)
    por_faixa.add_argument("--reducao", type=int, default=2, help="fator de redução (padrão 2)")

    camadas = comandos.add_parser("camadas", help="uma imagem por família de tinta")
    camadas.add_argument("alvos", nargs="+", type=Path)
    camadas.add_argument("--saida", type=Path, default=None)
    camadas.add_argument("--reducao", type=int, default=1, help="fator de redução (padrão 1)")

    args = parser.parse_args(argv)
    if args.comando == "inventario":
        cmd_inventario(args.pasta, args.reducao)
    elif args.comando == "faixas":
        cmd_faixas(args.alvos, args.reducao)
    else:
        cmd_camadas(args.alvos, args.saida, args.reducao)
    return 0


if __name__ == "__main__":
    sys.exit(main())
