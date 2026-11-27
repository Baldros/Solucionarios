"""Escreve as correções sobre a página manuscrita, como a caneta de um professor.

A página corrigida mostra onde está cada ponto: contorna, sublinha, risca,
marca o que está certo, indica onde falta algo e deixa notas curtas e numeradas
(①, ②, …). A explicação completa de cada número continua no feedback em texto.

A cor vem do diagnóstico, nunca de uma escolha avulsa: vermelho para erro
(de escrita ou conceitual), laranja para omissão ou gap e verde para o ✓ do que
está certo. Tudo é gravado em <pasta da imagem>/.correcoes/, pasta oculta que o
inventário da tinta ignora; o manuscrito original nunca é alterado.

Uso, a partir da raiz do repositório:

    .venv\\Scripts\\python -X utf8 .agents/skills/consolidar-exercicio/ferramentas/caneta.py <comando> ...

Comandos:

    grade <imagem|pasta>...     grava .correcoes/<nome>.grade.png: a página com uma
                                grade em porcentagem e as faixas de tinta numeradas
                                na margem direita, para localizar cada trecho.
    anotar <roteiro.json>...    desenha as marcas do roteiro e grava a página
                                corrigida ao lado dele, como <nome>.png.

O roteiro de Q2/6.png fica em Q2/.correcoes/6.json:

    {
      "marcas": [
        {"tipo": "contornar", "problema": "erro", "area": [16, 36, 86, 41], "n": 1,
         "nota": "a mesma inclusão escrita ao contrário"},
        {"tipo": "inserir", "problema": "omissao", "area": [40, 52, 44, 54], "n": 2,
         "nota": "falta o sentido A∩B ⊆ X"},
        {"tipo": "certo", "area": [18, 81, 45, 86]}
      ]
    }

- "imagem" (opcional): caminho relativo ao roteiro. Por padrão, a imagem de mesmo
  nome na pasta que contém .correcoes/.
- "area": [x0, y0, x1, y1] em porcentagem da largura e da altura, lida na grade.
  Em contornar, caixa, sublinhar, riscar e certo, a área encolhe até a tinta que
  contém; uma área folgada basta. "ajustar": false desliga o ajuste.
- "tipo": contornar, caixa, sublinhar, riscar, certo, inserir (circunflexo de
  inserção na base da área) ou nota (só o texto).
- "problema": "erro" ou "omissao", obrigatório em toda marca exceto o ✓ (certo),
  que é sempre verde e não leva problema. Marcas com o mesmo número podem ter
  problemas diferentes, quando um lapso encobre uma justificativa ausente.
- "n": número do ponto no feedback. "nota": texto curto, com símbolos Unicode
  (⊆ ∩ ∧ ∀ ⟹ ∉ …), colocado onde há menos tinta; "nota_em": [x, y] fixa seu
  canto superior esquerdo, em porcentagem.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

import tinta

PASTA = ".correcoes"
# A cor de cada marca é decidida pelo diagnóstico. As cópias em .correcoes/ ficam
# fora do inventário, então o vermelho do erro não se mistura à abertura vermelha
# do estudante.
CORES = {
    "erro": (205, 32, 38),  # lapso de escrita ou erro conceitual
    "omissao": (230, 125, 0),  # omissão ou gap
    "certo": (28, 140, 64),  # o ✓ do que está correto
}
PROBLEMAS = {"erro": "erro", "omissao": "omissao", "omissão": "omissao"}
FUNDO_NOTA = (255, 255, 255, 230)
COR_GRADE = (0, 150, 190)

TIPOS = ("contornar", "caixa", "sublinhar", "riscar", "certo", "inserir", "nota")
AJUSTAVEIS = {"contornar", "caixa", "sublinhar", "riscar", "certo"}
CHAVES_MARCA = {"tipo", "problema", "area", "n", "nota", "nota_em", "ajustar"}
CHAVES_ROTEIRO = {"imagem", "marcas"}

# Medidas em unidades u = largura da página / 100.
TRACO = 0.3  # espessura da caneta
LETRA = 2.1  # tamanho do texto das notas
FOLGA = 0.7  # distância entre a tinta e o traço que a contorna
AFASTAMENTO = 1.2  # distância mínima entre a nota e a marca
NOTA_LARGURA = 36  # largura máxima da nota, em porcentagem da página
AJUSTE_MIN = 20  # pixels de tinta abaixo dos quais a área não é ajustada

# A fonte manuscrita escreve as palavras; os símbolos que faltarem nela vêm da
# primeira fonte seguinte que os tenha. O Pillow procura as fontes do sistema.
FONTES_TEXTO = [("segoepr.ttf", 0), ("DejaVuSans.ttf", 0)]
FONTES_SIMBOLOS = [("cambria.ttc", 1), ("seguisym.ttf", 0), ("DejaVuSans.ttf", 0)]
FONTES_NUMERO = [("segoeuib.ttf", 0), ("DejaVuSans-Bold.ttf", 0)]


@dataclass(frozen=True)
class Caixa:
    x0: float
    y0: float
    x1: float
    y1: float

    @property
    def largura(self) -> float:
        return self.x1 - self.x0

    @property
    def altura(self) -> float:
        return self.y1 - self.y0

    @property
    def centro(self) -> tuple[float, float]:
        return (self.x0 + self.x1) / 2, (self.y0 + self.y1) / 2

    def expandir(self, m: float) -> Caixa:
        return Caixa(self.x0 - m, self.y0 - m, self.x1 + m, self.y1 + m)

    def intersecao(self, outra: Caixa) -> float:
        dx = min(self.x1, outra.x1) - max(self.x0, outra.x0)
        dy = min(self.y1, outra.y1) - max(self.y0, outra.y0)
        return max(dx, 0.0) * max(dy, 0.0)

    def distancia(self, outra: Caixa) -> float:
        dx = max(outra.x0 - self.x1, self.x0 - outra.x1, 0.0)
        dy = max(outra.y0 - self.y1, self.y0 - outra.y1, 0.0)
        return math.hypot(dx, dy)


def pontos_proximos(a: Caixa, b: Caixa) -> tuple[tuple[float, float], tuple[float, float]]:
    """Os pontos mais próximos entre duas caixas, um em cada borda."""

    def eixo(a0: float, a1: float, b0: float, b1: float) -> tuple[float, float]:
        if a1 < b0:
            return a1, b0
        if b1 < a0:
            return a0, b1
        meio = (max(a0, b0) + min(a1, b1)) / 2
        return meio, meio

    ax, bx = eixo(a.x0, a.x1, b.x0, b.x1)
    ay, by = eixo(a.y0, a.y1, b.y0, b.y1)
    return (ax, ay), (bx, by)


def borda_arredondada(c: Caixa, p: tuple[float, float]) -> tuple[float, float]:
    """O ponto do contorno arredondado (cápsula inscrita na caixa) mais próximo de p."""
    r = min(c.largura, c.altura) / 2
    cx, cy = c.centro
    if c.largura >= c.altura:
        (ax, ay), (bx, by) = (c.x0 + r, cy), (c.x1 - r, cy)
    else:
        (ax, ay), (bx, by) = (cx, c.y0 + r), (cx, c.y1 - r)
    comprimento = (bx - ax) ** 2 + (by - ay) ** 2
    s = 0.0 if comprimento == 0 else ((p[0] - ax) * (bx - ax) + (p[1] - ay) * (by - ay)) / comprimento
    s = min(max(s, 0.0), 1.0)
    qx, qy = ax + s * (bx - ax), ay + s * (by - ay)
    d = math.hypot(p[0] - qx, p[1] - qy)
    if d == 0:
        return p
    return qx + r * (p[0] - qx) / d, qy + r * (p[1] - qy) / d


# ─── Roteiro ─────────────────────────────────────────────────────────────


def _numeros(valor: object, tamanho: int) -> bool:
    return (
        isinstance(valor, list)
        and len(valor) == tamanho
        and all(isinstance(v, (int, float)) and not isinstance(v, bool) and 0 <= v <= 100 for v in valor)
    )


def validar(roteiro: object) -> list[str]:
    """Erros do roteiro, em português; lista vazia se ele estiver correto."""
    if not isinstance(roteiro, dict):
        return ["o roteiro deve ser um objeto JSON com a lista 'marcas'."]
    erros = [f"chave desconhecida no roteiro: '{c}'." for c in sorted(set(roteiro) - CHAVES_ROTEIRO)]
    marcas = roteiro.get("marcas")
    if not isinstance(marcas, list) or not marcas:
        return erros + ["'marcas' deve ser uma lista não vazia."]
    for i, marca in enumerate(marcas, start=1):
        onde = f"marca {i}"
        if not isinstance(marca, dict):
            erros.append(f"{onde}: deve ser um objeto.")
            continue
        erros += [f"{onde}: chave desconhecida '{c}'." for c in sorted(set(marca) - CHAVES_MARCA)]
        tipo = marca.get("tipo")
        if tipo not in TIPOS:
            erros.append(f"{onde}: tipo '{tipo}' inválido; use {', '.join(TIPOS)}.")
        if "area" in marca:
            area = marca["area"]
            if not _numeros(area, 4):
                erros.append(f"{onde}: 'area' deve ser [x0, y0, x1, y1] em porcentagem (0 a 100).")
            elif area[0] >= area[2] or area[1] >= area[3]:
                erros.append(f"{onde}: em 'area', x0 < x1 e y0 < y1.")
        elif tipo != "nota" or "nota_em" not in marca:
            erros.append(f"{onde}: falta 'area'.")
        if "nota_em" in marca and not _numeros(marca["nota_em"], 2):
            erros.append(f"{onde}: 'nota_em' deve ser [x, y] em porcentagem (0 a 100).")
        if "nota" in marca and not (isinstance(marca["nota"], str) and marca["nota"].strip()):
            erros.append(f"{onde}: 'nota' deve ser um texto não vazio.")
        if tipo == "nota" and "nota" not in marca:
            erros.append(f"{onde}: o tipo 'nota' precisa do texto em 'nota'.")
        if "n" in marca and not (isinstance(marca["n"], int) and not isinstance(marca["n"], bool) and marca["n"] > 0):
            erros.append(f"{onde}: 'n' deve ser um inteiro positivo.")
        if "ajustar" in marca and not isinstance(marca["ajustar"], bool):
            erros.append(f"{onde}: 'ajustar' deve ser true ou false.")
        if tipo == "certo":
            if "problema" in marca:
                erros.append(f"{onde}: o ✓ (certo) não leva 'problema'.")
        elif "problema" not in marca:
            erros.append(f"{onde}: falta 'problema': \"erro\" ou \"omissao\".")
        elif marca["problema"] not in PROBLEMAS:
            erros.append(f"{onde}: problema '{marca['problema']}' inválido; use \"erro\" ou \"omissao\".")
    return erros


def cor_da(marca: dict) -> tuple[int, int, int]:
    """A cor da marca segundo o diagnóstico: erro, omissão ou ✓."""
    if marca["tipo"] == "certo":
        return CORES["certo"]
    return CORES[PROBLEMAS[marca["problema"]]]


def imagem_do_roteiro(caminho: Path, roteiro: dict) -> Path:
    if "imagem" in roteiro:
        imagem = (caminho.parent / roteiro["imagem"]).resolve()
        if not imagem.is_file():
            raise FileNotFoundError(f"imagem do roteiro não encontrada: {imagem}")
        return imagem
    base = caminho.parent.parent if caminho.parent.name == PASTA else caminho.parent
    candidatas = [
        p for p in base.iterdir() if p.is_file() and p.stem == caminho.stem and p.suffix.lower() in tinta.EXTENSOES
    ]
    if len(candidatas) != 1:
        raise FileNotFoundError(
            f"não há uma única imagem '{caminho.stem}' em {base}; indique 'imagem' no roteiro."
        )
    return candidatas[0]


# ─── Escrita ─────────────────────────────────────────────────────────────


def carregar_fontes(lista: list[tuple[str, int]], tamanho: int) -> list[ImageFont.FreeTypeFont]:
    fontes = []
    for nome, indice in lista:
        try:
            fontes.append(ImageFont.truetype(nome, tamanho, index=indice))
        except OSError:
            continue
    return fontes or [ImageFont.load_default(tamanho)]


def _desenho(fonte: ImageFont.FreeTypeFont, caractere: str) -> bytes:
    lado = int(fonte.size * 2)
    img = Image.new("L", (lado, lado), 0)
    ImageDraw.Draw(img).text((lado // 4, lado // 4), caractere, font=fonte, fill=255)
    return img.tobytes()


OPERADORES = set("=≠<>≤≥∈∉⊆⊇⊂⊃⊊∩∪∧∨¬⟹⟸⟺⇒⇐⇔→←↔↦+−×·∘∖")


def unidades(paragrafo: str) -> list[str]:
    """As palavras do parágrafo, com cada operador isolado preso aos vizinhos.

    Assim "A∩B ⊆ X" não se parte entre linhas.
    """
    palavras = [p for p in paragrafo.split(" ") if p]
    resultado: list[str] = []
    prender = False
    for palavra in palavras:
        operador = all(c in OPERADORES for c in palavra)
        if resultado and (prender or operador):
            resultado[-1] += " " + palavra
        else:
            resultado.append(palavra)
        prender = operador
    return resultado


class Escrita:
    """Texto manuscrito com símbolos matemáticos emprestados de outra fonte."""

    def __init__(self, tamanho: int):
        self.tamanho = tamanho
        self.fontes = carregar_fontes(FONTES_TEXTO, tamanho) + carregar_fontes(FONTES_SIMBOLOS, tamanho)
        self.altura_linha = round(1.4 * tamanho)
        self.base = round(1.0 * tamanho)  # da borda de cima da linha até a linha de base
        self._sem_glifo = {id(f): _desenho(f, "\U0010fffd") for f in self.fontes}
        self._fonte_de: dict[str, ImageFont.FreeTypeFont] = {}

    def fonte(self, caractere: str) -> ImageFont.FreeTypeFont:
        if caractere not in self._fonte_de:
            self._fonte_de[caractere] = next(
                (
                    f
                    for f in self.fontes
                    if caractere.isspace() or _desenho(f, caractere) != self._sem_glifo[id(f)]
                ),
                self.fontes[0],
            )
        return self._fonte_de[caractere]

    def trechos(self, linha: str) -> list[tuple[ImageFont.FreeTypeFont, str]]:
        resultado: list[tuple[ImageFont.FreeTypeFont, str]] = []
        for c in linha:
            f = self.fonte(c)
            if resultado and resultado[-1][0] is f:
                resultado[-1] = (f, resultado[-1][1] + c)
            else:
                resultado.append((f, c))
        return resultado

    def largura(self, linha: str) -> float:
        return sum(f.getlength(t) for f, t in self.trechos(linha))

    def quebrar(self, texto: str, largura_max: float) -> list[str]:
        linhas = []
        for paragrafo in texto.split("\n"):
            atual = ""
            for palavra in unidades(paragrafo):
                teste = f"{atual} {palavra}" if atual else palavra
                if atual and self.largura(teste) > largura_max:
                    linhas.append(atual)
                    atual = palavra
                else:
                    atual = teste
            linhas.append(atual)
        return linhas

    def escrever(self, desenho: ImageDraw.ImageDraw, x: float, topo: float, linha: str, cor) -> None:
        for f, trecho in self.trechos(linha):
            desenho.text((x, topo + self.base), trecho, font=f, fill=cor, anchor="ls")
            x += f.getlength(trecho)


# ─── Página ──────────────────────────────────────────────────────────────


class Pagina:
    """A imagem, sua tinta e as regiões já ocupadas pelas correções."""

    def __init__(self, rgb: np.ndarray):
        self.rgb = rgb
        self.altura, self.largura = rgb.shape[:2]
        self.u = self.largura / 100
        self.tinta = tinta.classificar(rgb) != tinta.FUNDO
        acumulada = self.tinta.astype(np.int32).cumsum(axis=0).cumsum(axis=1)
        self._integral = np.pad(acumulada, ((1, 0), (1, 0)))
        self.ocupadas: list[Caixa] = []

    def px(self, area: list[float]) -> Caixa:
        x0, y0, x1, y1 = area
        return Caixa(
            x0 * self.largura / 100, y0 * self.altura / 100, x1 * self.largura / 100, y1 * self.altura / 100
        )

    def ponto(self, xy: list[float]) -> tuple[float, float]:
        return xy[0] * self.largura / 100, xy[1] * self.altura / 100

    def ajustar(self, caixa: Caixa) -> Caixa:
        """Encolhe a caixa até a tinta que ela contém, ignorando pontos isolados."""
        x0, y0 = max(0, int(caixa.x0)), max(0, int(caixa.y0))
        x1, y1 = min(self.largura, math.ceil(caixa.x1)), min(self.altura, math.ceil(caixa.y1))
        ys, xs = np.nonzero(self.tinta[y0:y1, x0:x1])
        if len(xs) < AJUSTE_MIN:
            return caixa
        qx0, qx1 = np.quantile(xs, [0.002, 0.998])
        qy0, qy1 = np.quantile(ys, [0.002, 0.998])
        return Caixa(x0 + float(qx0), y0 + float(qy0), x0 + float(qx1) + 1, y0 + float(qy1) + 1)

    def fracao_tinta(self, caixa: Caixa) -> float:
        x0, y0 = max(0, int(caixa.x0)), max(0, int(caixa.y0))
        x1, y1 = min(self.largura, int(caixa.x1)), min(self.altura, int(caixa.y1))
        if x1 <= x0 or y1 <= y0:
            return 0.0
        i = self._integral
        soma = i[y1, x1] - i[y0, x1] - i[y1, x0] + i[y0, x0]
        return float(soma) / ((x1 - x0) * (y1 - y0))

    def cobertura(self, caixa: Caixa) -> float:
        """Fração da caixa sobre correções já colocadas."""
        area = caixa.largura * caixa.altura
        return sum(caixa.intersecao(o) for o in self.ocupadas) / area if area else 0.0

    def tinta_no_caminho(self, p: tuple[float, float], q: tuple[float, float]) -> float:
        """Fração do segmento pq que atravessa tinta: uma seta não deve riscar o texto."""
        r = 0.4 * self.u
        amostras = [
            (p[0] + k / 20 * (q[0] - p[0]), p[1] + k / 20 * (q[1] - p[1])) for k in range(1, 20)
        ]
        return sum(self.fracao_tinta(Caixa(x - r, y - r, x + r, y + r)) > 0.05 for x, y in amostras) / 19

    def posicionar(self, largura: float, altura: float, alvo: Caixa) -> Caixa:
        """O lugar da nota perto do alvo com menos tinta e sem cobrir outra correção."""
        a = AFASTAMENTO * self.u
        borda = self.u
        cx, cy = alvo.centro
        xs = [alvo.x0, cx - largura / 2, alvo.x1 - largura, alvo.x1 + a, alvo.x0 - a - largura, borda,
              self.largura - largura - borda]
        xs += [p * self.largura / 100 for p in range(0, 100, 5)]
        passo = altura / 2
        ys = [cy - altura / 2, alvo.y0, alvo.y1 - altura]
        ys += [alvo.y1 + a + k * passo for k in range(8)]
        ys += [alvo.y0 - a - altura - k * passo for k in range(8)]
        # Encostar nas correções já colocadas aproveita as vagas entre elas.
        for o in self.ocupadas:
            xs += [o.x1 + a / 2, o.x0 - a / 2 - largura]
            ys += [o.y1 + a / 2, o.y0 - a / 2 - altura]
        melhor, menor = None, math.inf
        for x in xs:
            x = min(max(x, borda), self.largura - largura - borda)
            for y in ys:
                y = min(max(y, borda), self.altura - altura - borda)
                c = Caixa(x, y, x + largura, y + altura)
                if c.intersecao(alvo.expandir(a / 2)) > 0:
                    continue
                origem, destino = pontos_proximos(c, alvo)
                custo = (
                    15 * self.fracao_tinta(c)
                    + 40 * self.cobertura(c)
                    + 2 * self.tinta_no_caminho(origem, destino)
                    + c.distancia(alvo) / (0.25 * self.largura)
                )
                if custo < menor:
                    melhor, menor = c, custo
        return melhor or Caixa(borda, borda, borda + largura, borda + altura)


# ─── Desenho ─────────────────────────────────────────────────────────────


@dataclass
class Nota:
    linhas: list[str]
    numero: int | None
    cor: tuple[int, int, int]
    caixa: Caixa | None = None


class Caneta:
    def __init__(self, pagina: Pagina):
        self.pagina = pagina
        u = pagina.u
        self.u = u
        self.traco = max(2, round(TRACO * u))
        self.escrita = Escrita(max(12, round(LETRA * u)))
        self.numeros = carregar_fontes(FONTES_NUMERO, max(10, round(0.75 * LETRA * u)))[0]
        self.diametro = round(1.05 * self.escrita.tamanho)
        self.margem = round(0.5 * u)
        # Os fundos das notas ficam por baixo das marcas e dos textos.
        self.camada_fundo = Image.new("RGBA", (pagina.largura, pagina.altura), (0, 0, 0, 0))
        self.camada = Image.new("RGBA", (pagina.largura, pagina.altura), (0, 0, 0, 0))
        self.desenho = ImageDraw.Draw(self.camada)

    # Marcas ----------------------------------------------------------------

    def marcar(self, tipo: str, alvo: Caixa, cor: tuple[int, int, int]) -> Caixa:
        """Desenha a marca e devolve a caixa que ela ocupa."""
        d, t, f = self.desenho, self.traco, FOLGA * self.u
        cx, cy = alvo.centro
        if tipo == "contornar":
            c = alvo.expandir(f)
            d.rounded_rectangle([c.x0, c.y0, c.x1, c.y1], radius=min(c.largura, c.altura) / 2, outline=cor, width=t)
            return c
        if tipo == "caixa":
            c = alvo.expandir(f)
            d.rectangle([c.x0, c.y0, c.x1, c.y1], outline=cor, width=t)
            return c
        if tipo == "sublinhar":
            y = alvo.y1 + f
            d.line([(alvo.x0, y), (alvo.x1, y)], fill=cor, width=t)
            return Caixa(alvo.x0, alvo.y0, alvo.x1, y + t)
        if tipo == "riscar":
            inclinacao = 0.15 * alvo.altura
            d.line([(alvo.x0 - f, cy + inclinacao), (alvo.x1 + f, cy - inclinacao)], fill=cor, width=t)
            return alvo
        if tipo == "certo":
            # À direita do trecho ou sobre seu canto superior direito, onde houver
            # menos tinta e nenhuma outra correção.
            s = min(max(0.7 * alvo.altura, 1.8 * self.u), 4 * self.u)
            lugares = [(alvo.x1 + f, cy), (alvo.x1 - 0.4 * s, alvo.y0 - 0.1 * s)]
            caixas = [Caixa(x, y - 0.55 * s, x + s, y + 0.4 * s) for x, y in lugares]
            i = min(
                range(2),
                key=lambda k: self.pagina.fracao_tinta(caixas[k].expandir(f)) + 5 * self.pagina.cobertura(caixas[k]),
            )
            x, y = lugares[i]
            pontos = [(x, y), (x + 0.35 * s, y + 0.4 * s), (x + s, y - 0.55 * s)]
            d.line(pontos, fill=cor, width=t, joint="curve")
            return caixas[i]
        if tipo == "inserir":
            s = 2.2 * self.u
            base = alvo.y1 + 0.3 * s
            pontos = [(cx - s / 2, base + s / 2), (cx, base - s / 2), (cx + s / 2, base + s / 2)]
            d.line(pontos, fill=cor, width=t, joint="curve")
            return Caixa(cx - s / 2, base - s / 2, cx + s / 2, base + s / 2)
        return alvo  # nota: só o texto

    def numero(self, n: int, x: float, y: float, cor: tuple[int, int, int]) -> None:
        """Número branco num disco da cor da marca, com canto superior esquerdo em (x, y)."""
        r = self.diametro / 2
        self.desenho.ellipse([x, y, x + 2 * r, y + 2 * r], fill=cor)
        self.desenho.text((x + r, y + r), str(n), font=self.numeros, fill="white", anchor="mm")

    def seta(self, origem: tuple[float, float], destino: tuple[float, float], cor: tuple[int, int, int]) -> None:
        (x0, y0), (x1, y1) = origem, destino
        if math.hypot(x1 - x0, y1 - y0) < 0.6 * self.u:
            return
        self.desenho.line([origem, destino], fill=cor, width=self.traco)
        angulo = math.atan2(y1 - y0, x1 - x0)
        ponta = 4 * self.traco
        self.desenho.polygon(
            [
                destino,
                (x1 - ponta * math.cos(angulo - 0.45), y1 - ponta * math.sin(angulo - 0.45)),
                (x1 - ponta * math.cos(angulo + 0.45), y1 - ponta * math.sin(angulo + 0.45)),
            ],
            fill=cor,
        )

    # Notas -----------------------------------------------------------------

    def preparar(self, texto: str, numero: int | None, cor: tuple[int, int, int]) -> tuple[Nota, float, float]:
        recuo = self.diametro + 0.5 * self.u if numero else 0
        largura_max = NOTA_LARGURA * self.u - recuo - 2 * self.margem
        linhas = self.escrita.quebrar(texto, largura_max)
        largura = recuo + max(self.escrita.largura(l) for l in linhas) + 2 * self.margem
        altura = max(len(linhas) * self.escrita.altura_linha, self.diametro) + 2 * self.margem
        return Nota(linhas, numero, cor), largura, altura

    def fundo(self, nota: Nota) -> None:
        c = nota.caixa
        ImageDraw.Draw(self.camada_fundo).rounded_rectangle(
            [c.x0, c.y0, c.x1, c.y1], radius=self.margem, fill=FUNDO_NOTA
        )

    def escrever(self, nota: Nota) -> None:
        c, m = nota.caixa, self.margem
        x = c.x0 + m
        if nota.numero:
            topo_numero = c.y0 + m + (self.escrita.altura_linha - self.diametro) / 2
            self.numero(nota.numero, x, max(c.y0 + m, topo_numero), nota.cor)
            x += self.diametro + 0.5 * self.u
        for i, linha in enumerate(nota.linhas):
            self.escrita.escrever(self.desenho, x, c.y0 + m + i * self.escrita.altura_linha, linha, nota.cor)


def anotar(caminho: Path, saida: Path | None = None) -> Path:
    """Desenha o roteiro sobre a imagem e devolve o caminho da página corrigida."""
    roteiro = json.loads(caminho.read_text(encoding="utf-8"))
    erros = validar(roteiro)
    if erros:
        raise ValueError(f"{caminho}:\n" + "\n".join(f"- {e}" for e in erros))
    imagem = imagem_do_roteiro(caminho, roteiro)
    rgb = tinta.carregar(imagem)
    pagina = Pagina(rgb)
    caneta = Caneta(pagina)

    # Primeiro as marcas, que reservam seu espaço; depois as notas, que o evitam.
    # Os ✓ vêm por último entre as marcas, para escolher um lado livre.
    marcas = roteiro["marcas"]
    ordem = sorted(range(len(marcas)), key=lambda i: marcas[i]["tipo"] == "certo")
    feitas: list = [None] * len(marcas)
    for indice in ordem:
        marca = marcas[indice]
        tipo = marca["tipo"]
        if "area" in marca:
            alvo = pagina.px(marca["area"])
            if tipo in AJUSTAVEIS and marca.get("ajustar", True):
                alvo = pagina.ajustar(alvo)
        else:
            x, y = pagina.ponto(marca["nota_em"])
            alvo = Caixa(x, y, x + 1, y + 1)
        ocupada = caneta.marcar(tipo, alvo, cor_da(marca))
        if tipo != "nota":
            pagina.ocupadas.append(ocupada.expandir(caneta.traco))
        feitas[indice] = (marca, ocupada)

    notas = []
    for marca, ocupada in feitas:
        n = marca.get("n")
        if "nota" not in marca:
            if n:
                caneta.numero(
                    n, ocupada.x0 - caneta.diametro * 0.8, ocupada.y0 - caneta.diametro * 0.8, cor_da(marca)
                )
            continue
        nota, largura, altura = caneta.preparar(marca["nota"], n, cor_da(marca))
        if "nota_em" in marca:
            x, y = pagina.ponto(marca["nota_em"])
            nota.caixa = Caixa(x, y, x + largura, y + altura)
        else:
            nota.caixa = pagina.posicionar(largura, altura, ocupada)
        pagina.ocupadas.append(nota.caixa)
        notas.append((nota, ocupada, marca["tipo"]))

    for nota, _, _ in notas:
        caneta.fundo(nota)
    for nota, ocupada, tipo in notas:
        if tipo != "nota":
            origem, destino = pontos_proximos(nota.caixa, ocupada)
            if tipo == "contornar":
                destino = borda_arredondada(ocupada, origem)
                origem, _ = pontos_proximos(nota.caixa, Caixa(*destino, *destino))
            caneta.seta(origem, destino, nota.cor)
        caneta.escrever(nota)

    pagina_rgba = Image.fromarray(rgb).convert("RGBA")
    pagina_rgba.alpha_composite(caneta.camada_fundo)
    pagina_rgba.alpha_composite(caneta.camada)
    destino = (saida / f"{caminho.stem}.png") if saida else caminho.with_suffix(".png")
    destino.parent.mkdir(parents=True, exist_ok=True)
    pagina_rgba.convert("RGB").save(destino, optimize=True)
    return destino


# ─── Grade ───────────────────────────────────────────────────────────────


def grade(caminho: Path, saida: Path | None = None) -> Path:
    """Grava a página com a grade em porcentagem e as faixas de tinta numeradas."""
    rgb = tinta.carregar(caminho)
    altura, largura = rgb.shape[:2]
    u = largura / 100
    img = Image.fromarray(rgb).convert("RGBA")
    camada = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    fonte = carregar_fontes(FONTES_NUMERO, max(10, round(1.3 * u)))[0]
    for p in range(5, 100, 5):
        forte = p % 10 == 0
        cor = (*COR_GRADE, 150 if forte else 70)
        x, y = p * largura / 100, p * altura / 100
        d.line([(x, 0), (x, altura)], fill=cor, width=2 if forte else 1)
        d.line([(0, y), (largura, y)], fill=cor, width=2 if forte else 1)
        if forte:
            for px, py, ancora in [(x, 2, "mt"), (x, altura - 2, "mb")]:
                d.text((px, py), str(p), font=fonte, fill=(*COR_GRADE, 255), anchor=ancora)
            for px, py, ancora in [(4, y, "lm"), (largura - 4, y, "rm")]:
                d.text((px, py), str(p), font=fonte, fill=(*COR_GRADE, 255), anchor=ancora)

    reducao = 2
    rotulos = tinta.classificar(tinta.carregar(caminho, reducao))
    cor_faixa = (180, 0, 160, 220)
    for n, faixa in enumerate(tinta.faixas(rotulos), start=1):
        y0, y1 = faixa.y0 * reducao, (faixa.y1 + 1) * reducao
        x = largura - 4.5 * u
        d.line([(x, y0), (x, y1)], fill=cor_faixa, width=4)
        d.text((x - 0.5 * u, (y0 + y1) / 2), f"F{n}", font=fonte, fill=cor_faixa, anchor="rm")

    img.alpha_composite(camada)
    pasta = saida or caminho.parent / PASTA
    pasta.mkdir(parents=True, exist_ok=True)
    destino = pasta / f"{caminho.stem}.grade.png"
    img.convert("RGB").save(destino, optimize=True)
    return destino


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Escreve as correções sobre a página manuscrita.")
    comandos = parser.add_subparsers(dest="comando", required=True)

    por_grade = comandos.add_parser("grade", help="página com grade em porcentagem e faixas de tinta")
    por_grade.add_argument("alvos", nargs="+", type=Path)
    por_grade.add_argument("--saida", type=Path, default=None)

    por_roteiro = comandos.add_parser("anotar", help="desenha as marcas de um roteiro JSON")
    por_roteiro.add_argument("roteiros", nargs="+", type=Path)
    por_roteiro.add_argument("--saida", type=Path, default=None)

    args = parser.parse_args(argv)
    falhas = 0
    if args.comando == "grade":
        for alvo in args.alvos:
            for caminho in tinta.listar_imagens(alvo):
                print(grade(caminho, args.saida).as_posix())
    else:
        for roteiro in args.roteiros:
            try:
                print(anotar(roteiro, args.saida).as_posix())
            except (ValueError, FileNotFoundError, json.JSONDecodeError) as erro:
                print(f"Erro: {erro}", file=sys.stderr)
                falhas += 1
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
