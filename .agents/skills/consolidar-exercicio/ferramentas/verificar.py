"""Verifica os arquivos compilados pela skill consolidar-exercicio.

Regras gerais, que valem para qualquer nota, inclusive as do Notas-de-Estudo
que recebem um [!insight]:

    dolar         $ em linha pareado em cada parágrafo e $$ em número par
    indicadora    \\mathbb{1} não renderiza no MathJax do Obsidian; use \\mathbf{1}
    callout       todo callout tem título específico, não vazio nem genérico
    callout-link  nenhum wikilink dentro de callout

Regras dos arquivos do Solucionários (solução, processo, erros históricos e extras):

    wikilink      nenhum wikilink: o Solucionários e o Notas-de-Estudo são vaults
                  separados, e a teoria é citada pelo nome, em texto simples
    vault         nenhum link obsidian:// nem caminho de Images/
    pagina        nada de páginas ou arquivos de imagem: escreve-se por conteúdo

Da solução (Exercício N.M.md):

    enunciado     começa por "## Enunciado" ou "## Concepção"
    callout-tipo  só callouts [!note], que são as reflexões azuis

Do processo (Exercício N.M - Processo de resolução.md):

    secoes        Ponto de partida, Ciclos de revisão e Síntese do aprendizado,
                  nessa ordem
    ponte         (aviso) gap em Ciclos de revisão sem nota teórica citada
                  nem indicação de ausência de cobertura no acervo

Do arquivo histórico de erros (Exercício N.M - Erros.md):

    secoes        Avaliação, Erros de raciocínio, Erros de escrita e
                  Incompletudes, nessa ordem
    ponte         (aviso) entrada de erro de raciocínio ou de incompletude que
                  não cita nenhuma nota do acervo nem diz que o acervo não cobre
                  o assunto

Dos extras (Extras no acervo.md, Extras fora do acervo.md):

    capitulo      as seções de primeiro nível são capítulos ("## Capítulo N")

Da pasta de capítulo:

    par           toda solução tem seu processo (ou erros históricos), e todo
                  registro tem sua solução

Uso, a partir da raiz do repositório:

    .venv\\Scripts\\python .agents/skills/consolidar-exercicio/ferramentas/verificar.py [caminhos...]

Sem caminhos, verifica os .md do repositório fora de pastas ocultas e de
Images/, menos o README.md. Sai com código 1 se houver erro; avisos não mudam
o código de saída.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

SECOES_ERROS = ["Avaliação", "Erros de raciocínio", "Erros de escrita", "Incompletudes"]
SECOES_COM_PONTE = {"Erros de raciocínio", "Incompletudes"}
SECOES_PROCESSO = ["Ponto de partida", "Ciclos de revisão", "Síntese do aprendizado"]
TITULOS_GENERICOS = {
    "nota", "notas", "note", "observação", "observações", "obs", "insight", "reflexão", "reflexões",
}
EXTRAS = {"Extras no acervo.md", "Extras fora do acervo.md"}

RE_SOLUCAO = re.compile(r"^Exercício \d+(?:\.\d+)*\.md$")
RE_ERROS = re.compile(r"^Exercício \d+(?:\.\d+)* - Erros\.md$")
RE_PROCESSO = re.compile(r"^Exercício \d+(?:\.\d+)* - Processo de resolução\.md$")
RE_CALLOUT = re.compile(r"^>\s*\[!([^\]]+)\][+-]?\s*(.*)$")
RE_PAGINA = re.compile(r"\bp[áa]g(?:ina|inas|\.)|\.(?:png|jpe?g|webp)\b", re.IGNORECASE)
RE_CITA_ACERVO = re.compile(r"\bnotas?\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇ]|\bacervo\b")
RE_INDICADORA = re.compile(r"\\mathbb\s*\{?\s*1")


@dataclass
class Achado:
    caminho: Path
    linha: int
    nivel: str  # "erro" ou "aviso"
    regra: str
    mensagem: str

    def formatar(self) -> str:
        try:
            exibido = self.caminho.resolve().relative_to(Path.cwd().resolve())
        except ValueError:
            exibido = self.caminho
        return f"{exibido.as_posix()}:{self.linha}: {self.nivel} [{self.regra}] {self.mensagem}"


def tipo(caminho: Path) -> str:
    nome = caminho.name
    if RE_PROCESSO.match(nome):
        return "processo"
    if RE_ERROS.match(nome):
        return "erros"
    if RE_SOLUCAO.match(nome):
        return "solucao"
    if nome in EXTRAS:
        return "extras"
    return "nota"


def _apagar(m: re.Match) -> str:
    """Troca o trecho por espaços, preservando as quebras de linha."""
    return re.sub(r"[^\n]", " ", m.group(0))


def sem_codigo(texto: str) -> str:
    """Remove blocos e trechos de código e cifrões escapados, mantendo as linhas."""
    texto = re.sub(r"^(```|~~~).*?^\1[^\n]*$", _apagar, texto, flags=re.S | re.M)
    texto = re.sub(r"`[^`\n]*`", _apagar, texto)
    return texto.replace("\\$", "  ")


def _vazia(linha: str) -> bool:
    return linha.lstrip("> \t") == ""


def checar_dolares(caminho: Path, texto: str) -> list[Achado]:
    achados = []
    blocos = [m.start() for m in re.finditer(r"\$\$", texto)]
    if len(blocos) % 2:
        linha = texto.count("\n", 0, blocos[-1]) + 1
        achados.append(Achado(caminho, linha, "erro", "dolar", "número ímpar de $$"))
    sem_blocos = re.sub(r"\$\$.*?\$\$", _apagar, texto, flags=re.S)
    inicio, contagem = None, 0
    for i, linha in enumerate(sem_blocos.split("\n") + [""], start=1):
        if _vazia(linha) or linha.startswith("#"):
            if inicio is not None and contagem % 2:
                achados.append(Achado(caminho, inicio, "erro", "dolar", "$ em linha sem par neste parágrafo"))
            inicio, contagem = None, 0
            if linha.startswith("#") and linha.count("$") % 2:
                achados.append(Achado(caminho, i, "erro", "dolar", "$ em linha sem par no título"))
            continue
        if inicio is None:
            inicio = i
        contagem += linha.count("$")
    return achados


def checar_callouts(caminho: Path, linhas: list[str], tipo_arquivo: str) -> list[Achado]:
    achados = []
    i = 0
    while i < len(linhas):
        m = RE_CALLOUT.match(linhas[i])
        if not m:
            i += 1
            continue
        tipo_callout = m.group(1).strip().lower()
        titulo = m.group(2).strip().strip("*_ ").strip()
        if not titulo:
            achados.append(Achado(caminho, i + 1, "erro", "callout", "callout sem título"))
        elif titulo.casefold() in TITULOS_GENERICOS:
            achados.append(Achado(caminho, i + 1, "erro", "callout", f"título genérico: {titulo!r}"))
        if tipo_arquivo == "solucao" and tipo_callout != "note":
            achados.append(
                Achado(caminho, i + 1, "erro", "callout-tipo", f"a solução só usa [!note], não [!{tipo_callout}]")
            )
        j = i
        while j < len(linhas) and linhas[j].startswith(">"):
            if tipo_arquivo == "nota" and "[[" in linhas[j]:
                achados.append(Achado(caminho, j + 1, "erro", "callout-link", "wikilink dentro de callout"))
            j += 1
        i = j
    return achados


def checar_solucionarios(caminho: Path, linhas: list[str]) -> list[Achado]:
    achados = []
    for n, linha in enumerate(linhas, start=1):
        if "[[" in linha:
            achados.append(Achado(caminho, n, "erro", "wikilink", "wikilink num arquivo do Solucionários"))
        if "obsidian://" in linha or "Images/" in linha:
            achados.append(Achado(caminho, n, "erro", "vault", "link ou caminho fora do conteúdo"))
        if RE_PAGINA.search(linha):
            achados.append(Achado(caminho, n, "erro", "pagina", "menção a página ou imagem do manuscrito"))
    return achados


def checar_solucao(caminho: Path, linhas: list[str]) -> list[Achado]:
    primeira = next(((n, l) for n, l in enumerate(linhas, start=1) if l.strip()), None)
    if primeira is None or primeira[1].strip() not in {"## Enunciado", "## Concepção"}:
        linha = primeira[0] if primeira else 1
        return [Achado(caminho, linha, "erro", "enunciado", 'a solução deve começar por "## Enunciado" ou "## Concepção"')]
    return []


def checar_registro(
    caminho: Path,
    linhas: list[str],
    secoes_esperadas: list[str],
    secoes_com_ponte: set[str],
) -> list[Achado]:
    achados = []
    secoes = [(n, l[3:].strip()) for n, l in enumerate(linhas, start=1) if l.startswith("## ")]
    nomes = [nome for _, nome in secoes]
    for esperada in secoes_esperadas:
        if esperada not in nomes:
            achados.append(Achado(caminho, 1, "erro", "secoes", f'falta a seção "## {esperada}"'))
    presentes = [nome for nome in nomes if nome in secoes_esperadas]
    if presentes != [s for s in secoes_esperadas if s in presentes]:
        achados.append(Achado(caminho, 1, "erro", "secoes", "seções fora da ordem: " + ", ".join(secoes_esperadas)))
    for n, nome in secoes:
        if nome not in secoes_esperadas:
            achados.append(Achado(caminho, n, "aviso", "secoes", f'seção inesperada: "## {nome}"'))

    secao_atual, entrada, inicio, corpo = None, None, 0, []

    def fechar():
        if entrada is not None and secao_atual in secoes_com_ponte:
            if not RE_CITA_ACERVO.search(" ".join([entrada, *corpo])):
                achados.append(
                    Achado(caminho, inicio, "aviso", "ponte", f'"{entrada}" não cita nota do acervo')
                )

    for n, linha in enumerate(linhas, start=1):
        if linha.startswith("## "):
            fechar()
            secao_atual, entrada, corpo = linha[3:].strip(), None, []
        elif linha.startswith("### "):
            fechar()
            entrada, inicio, corpo = linha[4:].strip(), n, []
        elif entrada is not None:
            corpo.append(linha)
    fechar()
    return achados


def checar_erros(caminho: Path, linhas: list[str]) -> list[Achado]:
    """Mantém a validação dos registros anteriores, sem migrá-los."""
    return checar_registro(caminho, linhas, SECOES_ERROS, SECOES_COM_PONTE)


def checar_processo(caminho: Path, linhas: list[str]) -> list[Achado]:
    return checar_registro(caminho, linhas, SECOES_PROCESSO, {"Ciclos de revisão"})


def checar_extras(caminho: Path, linhas: list[str]) -> list[Achado]:
    return [
        Achado(caminho, n, "erro", "capitulo", f'seção que não é capítulo: "{l.strip()}"')
        for n, l in enumerate(linhas, start=1)
        if l.startswith("## ") and not l[3:].strip().startswith("Capítulo")
    ]


def checar_par(caminho: Path, tipo_arquivo: str) -> list[Achado]:
    if tipo_arquivo == "solucao":
        processo = caminho.with_name(caminho.stem + " - Processo de resolução.md")
        legado = caminho.with_name(caminho.stem + " - Erros.md")
        if not processo.exists() and not legado.exists():
            return [Achado(caminho, 1, "erro", "par", f'falta o processo de resolução "{processo.name}" (ou um registro histórico de erros)')]
    elif tipo_arquivo in {"processo", "erros"}:
        sufixo = " - Processo de resolução.md" if tipo_arquivo == "processo" else " - Erros.md"
        par = caminho.with_name(caminho.name.removesuffix(sufixo) + ".md")
        if not par.exists():
            return [Achado(caminho, 1, "erro", "par", f'falta a solução "{par.name}"')]
    return []


def verificar_arquivo(caminho: Path, texto: str | None = None) -> list[Achado]:
    if texto is None:
        texto = caminho.read_text(encoding="utf-8")
    limpo = sem_codigo(texto)
    linhas = limpo.split("\n")
    tipo_arquivo = tipo(caminho)
    achados = checar_dolares(caminho, limpo)
    achados += [
        Achado(caminho, n, "erro", "indicadora", r"\mathbb{1} não renderiza; use \mathbf{1}")
        for n, linha in enumerate(linhas, start=1)
        if RE_INDICADORA.search(linha)
    ]
    achados += checar_callouts(caminho, linhas, tipo_arquivo)
    if tipo_arquivo != "nota":
        achados += checar_solucionarios(caminho, linhas)
    if tipo_arquivo == "solucao":
        achados += checar_solucao(caminho, linhas)
    elif tipo_arquivo == "processo":
        achados += checar_processo(caminho, linhas)
    elif tipo_arquivo == "erros":
        achados += checar_erros(caminho, linhas)
    elif tipo_arquivo == "extras":
        achados += checar_extras(caminho, linhas)
    achados += checar_par(caminho, tipo_arquivo)
    return sorted(achados, key=lambda a: a.linha)


def raiz_do_repositorio() -> Path:
    for pasta in Path(__file__).resolve().parents:
        if (pasta / ".obsidian").is_dir():
            return pasta
    return Path.cwd()


def coletar(alvos: list[Path]) -> list[Path]:
    if not alvos:
        raiz = raiz_do_repositorio()
        return sorted(
            p
            for p in raiz.rglob("*.md")
            if not any(parte.startswith(".") or parte == "Images" for parte in p.relative_to(raiz).parts)
            and p.relative_to(raiz).as_posix() != "README.md"
        )
    arquivos = []
    for alvo in alvos:
        arquivos += sorted(alvo.rglob("*.md")) if alvo.is_dir() else [alvo]
    return arquivos


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Verifica os arquivos compilados pela skill consolidar-exercicio.")
    parser.add_argument("caminhos", nargs="*", type=Path)
    args = parser.parse_args(argv)

    arquivos = coletar(args.caminhos)
    achados = [a for caminho in arquivos for a in verificar_arquivo(caminho)]
    for achado in achados:
        print(achado.formatar())
    erros = sum(a.nivel == "erro" for a in achados)
    avisos = len(achados) - erros
    print(f"{erros} erro(s), {avisos} aviso(s) em {len(arquivos)} arquivo(s).")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
