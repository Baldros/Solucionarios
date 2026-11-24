"""Testes das regras do verificar.py, com arquivos escritos numa pasta temporária."""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import verificar  # noqa: E402

SOLUCAO = """## Enunciado

Seja $X$ tal que $A\\subseteq X$ e $B\\subseteq X$.

> [!note] O menor conjunto que contém A e B
> A propriedade diz que $X$ é o **menor** deles.

## Demonstração

$$
X=A\\cup B.
$$

Pela antissimetria da inclusão, $X=A\\cup B$. $\\blacksquare$
"""

ERROS = """Erros da tentativa.

## Avaliação

A tentativa prova uma inclusão.

## Erros de raciocínio

### Um erro com a teoria citada

A antissimetria está na nota Subconjunto.

## Erros de escrita

### Parênteses omitidos

Escrita sem nota, o que é aceito nesta seção.

## Incompletudes

### Algo que o acervo não cobre

O acervo não tem notas de lógica.
"""


PROCESSO_HISTORICO = """Registro das orientações e revisões observadas na conversa.

## Ponto de partida

A tentativa já tinha uma inclusão e precisava justificar a recíproca.

## Ciclos de revisão

### Distinguir as duas direções

Foi retomada a definição de inclusão da nota Subconjunto. Depois da orientação,
o usuário reformulou a recíproca e a justificou na versão revista.

### Explicitar uma regra lógica

O acervo não cobre a regra formal. O encaminhamento para estudo foi combinado.

## Síntese do aprendizado

A versão final justifica as duas inclusões e conclui pela antissimetria.
"""


PROCESSO = """Análise técnica dos problemas e de suas correções.

## Abordagem inicial

A estratégia por dupla inclusão já fornecia um dos sentidos.

## Problemas e correções

### Distinguir as duas direções

Pela definição da nota Subconjunto, cada inclusão exige uma direção da
implicação por elementos. A inclusão contrária completa a igualdade.

### Explicitar uma regra lógica

O acervo não cobre a regra formal de aplicação da hipótese universal.

## Síntese técnica

A resposta justifica as duas inclusões e conclui pela antissimetria.
"""


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.pasta = Path(self._tmp.name) / "Capítulo 1"
        self.pasta.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def escrever(self, nome, texto):
        caminho = self.pasta / nome
        caminho.write_text(texto, encoding="utf-8")
        return caminho

    def regras(self, caminho):
        return {(a.regra, a.nivel) for a in verificar.verificar_arquivo(caminho)}


class TestArquivosLimpos(Base):
    def test_solucao_e_erros_limpos(self):
        solucao = self.escrever("Exercício 9.9.md", SOLUCAO)
        erros = self.escrever("Exercício 9.9 - Erros.md", ERROS)
        self.assertEqual(self.regras(solucao), set())
        self.assertEqual(self.regras(erros), set())


class TestRegrasGerais(Base):
    def test_dolar_sem_par(self):
        self.escrever("Exercício 9.9 - Erros.md", ERROS)
        caminho = self.escrever("Exercício 9.9.md", SOLUCAO.replace("Seja $X$", "Seja $X"))
        self.assertIn(("dolar", "erro"), self.regras(caminho))

    def test_blocos_impares(self):
        caminho = self.escrever("Nota.md", "Texto.\n\n$$\nx=1\n")
        self.assertIn(("dolar", "erro"), self.regras(caminho))

    def test_codigo_nao_conta_dolar(self):
        caminho = self.escrever("Nota.md", "Use `$` para abrir a fórmula.\n")
        self.assertEqual(self.regras(caminho), set())

    def test_indicadora(self):
        caminho = self.escrever("Nota.md", "A indicadora $\\mathbb{1}_A$.\n")
        self.assertIn(("indicadora", "erro"), self.regras(caminho))

    def test_callout_sem_titulo_e_generico(self):
        sem_titulo = self.escrever("A.md", "> [!note]\n> Texto.\n")
        generico = self.escrever("B.md", "> [!note] Nota\n> Texto.\n")
        self.assertIn(("callout", "erro"), self.regras(sem_titulo))
        self.assertIn(("callout", "erro"), self.regras(generico))

    def test_wikilink_na_nota_so_dentro_de_callout(self):
        corpo = self.escrever("Corpo.md", "A [[Subconjunto|inclusão]] é ampla.\n")
        callout = self.escrever("Callout.md", "> [!insight] A estrita é irreflexiva\n> Ver [[Subconjunto]].\n")
        self.assertEqual(self.regras(corpo), set())
        self.assertIn(("callout-link", "erro"), self.regras(callout))


class TestSolucionarios(Base):
    def test_wikilink_vault_e_pagina(self):
        self.escrever("Exercício 9.9 - Erros.md", ERROS)
        texto = SOLUCAO + "\nVer [[Subconjunto]], obsidian://open e a página 5.\n"
        regras = self.regras(self.escrever("Exercício 9.9.md", texto))
        self.assertTrue({("wikilink", "erro"), ("vault", "erro"), ("pagina", "erro")} <= regras)

    def test_solucao_comeca_pelo_enunciado(self):
        self.escrever("Exercício 9.9 - Erros.md", ERROS)
        caminho = self.escrever("Exercício 9.9.md", SOLUCAO.replace("## Enunciado", "## Demonstração inicial"))
        self.assertIn(("enunciado", "erro"), self.regras(caminho))

    def test_solucao_so_usa_note(self):
        self.escrever("Exercício 9.9 - Erros.md", ERROS)
        caminho = self.escrever("Exercício 9.9.md", SOLUCAO.replace("[!note]", "[!insight]"))
        self.assertIn(("callout-tipo", "erro"), self.regras(caminho))

    def test_secao_faltando_e_fora_de_ordem(self):
        self.escrever("Exercício 9.9.md", SOLUCAO)
        faltando = self.escrever("Exercício 9.9 - Erros.md", ERROS.replace("## Incompletudes", "## Outras"))
        self.assertIn(("secoes", "erro"), self.regras(faltando))
        trocado = ERROS.replace("## Erros de escrita", "## TROCA").replace("## Erros de raciocínio", "## Erros de escrita")
        trocado = trocado.replace("## TROCA", "## Erros de raciocínio")
        fora_de_ordem = self.escrever("Exercício 9.9 - Erros.md", trocado)
        self.assertIn(("secoes", "erro"), self.regras(fora_de_ordem))

    def test_ponte_com_a_teoria(self):
        self.escrever("Exercício 9.9.md", SOLUCAO)
        sem_nota = ERROS.replace("A antissimetria está na nota Subconjunto.", "Faltou a outra inclusão.")
        caminho = self.escrever("Exercício 9.9 - Erros.md", sem_nota)
        achados = verificar.verificar_arquivo(caminho)
        ponte = [a for a in achados if a.regra == "ponte"]
        self.assertEqual(len(ponte), 1)
        self.assertEqual(ponte[0].nivel, "aviso")
        self.assertIn("Um erro com a teoria citada", ponte[0].mensagem)

    def test_par_de_arquivos(self):
        solucao = self.escrever("Exercício 9.9.md", SOLUCAO)
        erros = self.escrever("Exercício 9.8 - Erros.md", ERROS)
        self.assertIn(("par", "erro"), self.regras(solucao))
        self.assertIn(("par", "erro"), self.regras(erros))

    def test_extras_por_capitulo(self):
        bom = self.escrever("Extras no acervo.md", "Intro.\n\n## Capítulo 1\n\n### Ligação\n\nTexto.\n")
        ruim = self.escrever("Extras fora do acervo.md", "Intro.\n\n## Exercício 1.1\n\n### Ligação\n\nTexto.\n")
        self.assertEqual(self.regras(bom), set())
        self.assertIn(("capitulo", "erro"), self.regras(ruim))


class TestProcessoDeResolucao(Base):
    def test_novo_par_sem_arquivo_de_erros(self):
        solucao = self.escrever("Exercício 9.9.md", SOLUCAO)
        processo = self.escrever("Exercício 9.9 - Processo de resolução.md", PROCESSO)
        self.assertEqual(verificar.tipo(processo), "processo")
        self.assertEqual(self.regras(solucao), set())
        self.assertEqual(self.regras(processo), set())

    def test_processo_nao_substitui_solucao_de_outro_exercicio(self):
        solucao = self.escrever("Exercício 9.9.md", SOLUCAO)
        processo = self.escrever("Exercício 9.8 - Processo de resolução.md", PROCESSO)
        self.assertIn(("par", "erro"), self.regras(solucao))
        self.assertIn(("par", "erro"), self.regras(processo))

    def test_secoes_do_processo_faltando_ou_fora_de_ordem(self):
        self.escrever("Exercício 9.9.md", SOLUCAO)
        caminho = self.escrever(
            "Exercício 9.9 - Processo de resolução.md",
            PROCESSO.replace("## Síntese técnica", "## Outras"),
        )
        self.assertIn(("secoes", "erro"), self.regras(caminho))
        trocado = PROCESSO.replace("## Abordagem inicial", "## TROCA")
        trocado = trocado.replace("## Problemas e correções", "## Abordagem inicial")
        trocado = trocado.replace("## TROCA", "## Problemas e correções")
        caminho.write_text(trocado, encoding="utf-8")
        self.assertIn(("secoes", "erro"), self.regras(caminho))

    def test_cada_gap_precisa_de_fundamentacao(self):
        self.escrever("Exercício 9.9.md", SOLUCAO)
        caminho = self.escrever(
            "Exercício 9.9 - Processo de resolução.md",
            PROCESSO.replace("da nota Subconjunto", "discutida na conversa"),
        )
        ponte = [a for a in verificar.verificar_arquivo(caminho) if a.regra == "ponte"]
        self.assertEqual(len(ponte), 1)
        self.assertEqual(ponte[0].nivel, "aviso")
        self.assertIn("Distinguir as duas direções", ponte[0].mensagem)

    def test_registro_sem_gaps_nao_exige_entrada_inventada(self):
        self.escrever("Exercício 9.9.md", SOLUCAO)
        caminho = self.escrever(
            "Exercício 9.9 - Processo de resolução.md",
            """Registro do processo.

## Abordagem inicial

A primeira tentativa já estava adequada à teoria.

## Problemas e correções

Não houve gap nem necessidade de correção.

## Síntese técnica

A abordagem inicial satisfaz o referencial sem desenvolvimento corretivo.
""",
        )
        self.assertEqual(self.regras(caminho), set())

    def test_processo_tambem_respeita_separacao_dos_vaults(self):
        self.escrever("Exercício 9.9.md", SOLUCAO)
        caminho = self.escrever(
            "Exercício 9.9 - Processo de resolução.md",
            PROCESSO + "\nVer [[Subconjunto]], obsidian://open e a página 5.\n",
        )
        self.assertTrue(
            {("wikilink", "erro"), ("vault", "erro"), ("pagina", "erro")}
            <= self.regras(caminho)
        )

    def test_abertura_concepcao_preserva_modelo_atual(self):
        self.escrever("Exercício 9.9 - Processo de resolução.md", PROCESSO)
        caminho = self.escrever(
            "Exercício 9.9.md", SOLUCAO.replace("## Enunciado", "## Concepção")
        )
        self.assertEqual(self.regras(caminho), set())

    def test_formato_historico_do_processo_continua_valido(self):
        self.escrever("Exercício 9.9.md", SOLUCAO)
        caminho = self.escrever("Exercício 9.9 - Processo de resolução.md", PROCESSO_HISTORICO)
        self.assertEqual(self.regras(caminho), set())

    def test_processo_historico_incompleto_ainda_e_detectado(self):
        self.escrever("Exercício 9.9.md", SOLUCAO)
        caminho = self.escrever(
            "Exercício 9.9 - Processo de resolução.md",
            PROCESSO_HISTORICO.replace("## Síntese do aprendizado", "## Outras"),
        )
        self.assertIn(("secoes", "erro"), self.regras(caminho))

    def test_misturar_os_dois_formatos_nao_forma_um_processo_valido(self):
        self.escrever("Exercício 9.9.md", SOLUCAO)
        caminho = self.escrever(
            "Exercício 9.9 - Processo de resolução.md",
            PROCESSO.replace("## Problemas e correções", "## Ciclos de revisão"),
        )
        self.assertIn(("secoes", "erro"), self.regras(caminho))


class TestEtapas(Base):
    def test_solucao_intermediaria_dispensa_so_o_processo_ausente(self):
        caminho = self.escrever("Exercício 9.9.md", SOLUCAO)
        self.assertEqual(verificar.verificar_arquivo(caminho, etapa="solucao"), [])
        self.assertIn(("par", "erro"), self.regras(caminho))
        completo = verificar.verificar_arquivo(caminho, etapa="completo")
        self.assertTrue(any(a.regra == "par" for a in completo))

    def test_etapa_solucao_mantem_as_demais_validacoes(self):
        texto = SOLUCAO.replace("## Enunciado", "## Demonstração") + "\nVer [[Subconjunto]].\n"
        caminho = self.escrever("Exercício 9.9.md", texto)
        regras = {(a.regra, a.nivel) for a in verificar.verificar_arquivo(caminho, etapa="solucao")}
        self.assertNotIn(("par", "erro"), regras)
        self.assertTrue({("enunciado", "erro"), ("wikilink", "erro")} <= regras)

    def test_registros_orfaos_continuam_invalidos_na_etapa_solucao(self):
        for nome, texto in [
            ("Exercício 9.9 - Processo de resolução.md", PROCESSO),
            ("Exercício 9.8 - Erros.md", ERROS),
        ]:
            with self.subTest(nome=nome):
                caminho = self.escrever(nome, texto)
                achados = verificar.verificar_arquivo(caminho, etapa="solucao")
                self.assertTrue(any(a.regra == "par" for a in achados))

    def test_etapa_solucao_nao_dispensa_validar_o_processo_presente(self):
        self.escrever("Exercício 9.9.md", SOLUCAO)
        caminho = self.escrever(
            "Exercício 9.9 - Processo de resolução.md",
            PROCESSO.replace("## Síntese técnica", "## Outras"),
        )
        achados = verificar.verificar_arquivo(caminho, etapa="solucao")
        self.assertTrue(any(a.regra == "secoes" and a.nivel == "erro" for a in achados))

    def test_cli_distingue_etapas_e_exige_par_ao_final(self):
        caminho = self.escrever("Exercício 9.9.md", SOLUCAO)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(verificar.main([str(caminho)]), 1)
            self.assertEqual(verificar.main(["--etapa", "solucao", str(caminho)]), 0)
            self.assertEqual(verificar.main(["--etapa", "completo", str(caminho)]), 1)
            self.escrever("Exercício 9.9 - Processo de resolução.md", PROCESSO)
            self.assertEqual(verificar.main([str(caminho), str(caminho.parent / "Exercício 9.9 - Processo de resolução.md")]), 0)

    def test_etapa_desconhecida_nao_e_aceita_pela_api(self):
        caminho = self.escrever("Exercício 9.9.md", SOLUCAO)
        with self.assertRaises(ValueError):
            verificar.verificar_arquivo(caminho, etapa="outra")


if __name__ == "__main__":
    unittest.main()
