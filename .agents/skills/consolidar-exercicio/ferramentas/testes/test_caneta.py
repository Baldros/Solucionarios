"""Testes da caneta de correção, com páginas sintéticas."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import caneta  # noqa: E402
import tinta  # noqa: E402


def pagina_sintetica():
    """Página 800×1000 com três linhas pretas e uma margem direita livre."""
    img = np.full((1000, 800, 3), 255, np.uint8)
    img[100:140, 60:500] = (20, 20, 20)
    img[300:340, 60:450] = (20, 20, 20)
    img[500:540, 60:480] = (20, 20, 20)
    return img


def roteiro_valido():
    return {
        "marcas": [
            {"tipo": "contornar", "problema": "omissao", "area": [5, 8, 65, 16], "n": 1,
             "nota": "gap: falta A∩B ⊆ X"},
            {"tipo": "certo", "area": [5, 28, 60, 36]},
            {"tipo": "nota", "problema": "erro", "nota_em": [10, 80], "nota": "conclusão sem base"},
        ]
    }


class TestRoteiro(unittest.TestCase):
    def test_roteiro_valido(self):
        self.assertEqual(caneta.validar(roteiro_valido()), [])

    def test_erros_apontam_a_marca(self):
        roteiro = {
            "marcas": [
                {"tipo": "circular", "area": [1, 2, 3, 4]},
                {"tipo": "riscar", "area": [10, 10, 5, 20]},
                {"tipo": "sublinhar", "area": [1, 2, 300, 4]},
                {"tipo": "nota", "area": [1, 2, 3, 4]},
                {"tipo": "caixa", "area": [1, 2, 3, 4], "notas": "x"},
                {"tipo": "certo"},
                {"tipo": "sublinhar", "area": [1, 2, 3, 4]},
                {"tipo": "certo", "problema": "erro", "area": [1, 2, 3, 4]},
                {"tipo": "caixa", "problema": "lapso", "area": [1, 2, 3, 4]},
            ]
        }
        erros = caneta.validar(roteiro)
        for trecho in [
            "marca 1: tipo 'circular'",
            "marca 2: em 'area'",
            "marca 3: 'area'",
            "marca 4: o tipo 'nota'",
            "marca 5: chave desconhecida 'notas'",
            "marca 6: falta 'area'",
            "marca 7: falta 'problema'",
            "marca 8: o ✓ (certo) não leva 'problema'",
            "marca 9: problema 'lapso' inválido",
        ]:
            self.assertTrue(any(e.startswith(trecho) for e in erros), (trecho, erros))

    def test_roteiro_sem_marcas(self):
        self.assertTrue(caneta.validar({"marcas": []}))
        self.assertTrue(caneta.validar([]))

    def test_operador_nao_parte_a_expressao(self):
        self.assertEqual(
            caneta.unidades("De onde sai A∩B ⊆ X? Qual Y"),
            ["De", "onde", "sai", "A∩B ⊆ X?", "Qual", "Y"],
        )
        self.assertEqual(caneta.unidades("X = A ∪ B e mais"), ["X = A ∪ B", "e", "mais"])


class TestGeometria(unittest.TestCase):
    def test_area_folgada_encolhe_ate_a_tinta(self):
        pagina = caneta.Pagina(pagina_sintetica())
        ajustada = pagina.ajustar(pagina.px([2, 7, 80, 18]))
        self.assertAlmostEqual(ajustada.x0, 60, delta=2)
        self.assertAlmostEqual(ajustada.x1, 500, delta=2)
        self.assertAlmostEqual(ajustada.y0, 100, delta=2)
        self.assertAlmostEqual(ajustada.y1, 140, delta=2)

    def test_area_sem_tinta_fica_como_esta(self):
        pagina = caneta.Pagina(pagina_sintetica())
        area = pagina.px([70, 70, 90, 90])
        self.assertEqual(pagina.ajustar(area), area)

    def test_nota_evita_tinta_e_correcoes(self):
        pagina = caneta.Pagina(pagina_sintetica())
        alvo = caneta.Caixa(60, 300, 450, 340)
        pagina.ocupadas.append(caneta.Caixa(60, 350, 800, 480))
        nota = pagina.posicionar(240, 60, alvo)
        self.assertEqual(pagina.fracao_tinta(nota), 0.0)
        self.assertEqual(pagina.cobertura(nota), 0.0)
        self.assertLess(nota.distancia(alvo), 150)

    def test_seta_chega_ao_contorno_arredondado(self):
        c = caneta.Caixa(0, 0, 200, 40)  # cápsula de raio 20 sobre o segmento y = 20
        x, y = caneta.borda_arredondada(c, (300, 20))
        self.assertAlmostEqual(x, 200)
        self.assertAlmostEqual(y, 20)
        x, y = caneta.borda_arredondada(c, (100, -50))
        self.assertAlmostEqual(x, 100)
        self.assertAlmostEqual(y, 0)


class TestArquivos(unittest.TestCase):
    def preparar(self, pasta: Path) -> tuple[Path, Path]:
        imagem = pasta / "Q1" / "6.png"
        imagem.parent.mkdir()
        Image.fromarray(pagina_sintetica()).save(imagem)
        roteiro = imagem.parent / caneta.PASTA / "6.json"
        roteiro.parent.mkdir()
        roteiro.write_text(json.dumps(roteiro_valido(), ensure_ascii=False), encoding="utf-8")
        return imagem, roteiro

    def test_anotar_grava_ao_lado_do_roteiro_sem_tocar_o_original(self):
        with tempfile.TemporaryDirectory() as tmp:
            imagem, roteiro = self.preparar(Path(tmp))
            antes = imagem.read_bytes()
            saida = caneta.anotar(roteiro)
            self.assertEqual(saida, roteiro.with_suffix(".png"))
            self.assertEqual(imagem.read_bytes(), antes)
            original, corrigida = tinta.carregar(imagem), tinta.carregar(saida)
            self.assertEqual(original.shape, corrigida.shape)
            mudou = (original != corrigida).any(axis=-1)
            self.assertGreater(mudou.sum(), 1000)
            self.assertFalse((tinta.classificar(corrigida)[mudou] == tinta.AZUL).any())

    def test_cor_segue_o_diagnostico(self):
        # Uma marca sem nota por linha: erro na primeira, omissão na segunda e ✓ na terceira.
        roteiro_cores = {
            "marcas": [
                {"tipo": "contornar", "problema": "erro", "area": [5, 8, 65, 16]},
                {"tipo": "sublinhar", "problema": "omissão", "area": [5, 28, 60, 36]},
                {"tipo": "certo", "area": [5, 48, 62, 56]},
            ]
        }
        with tempfile.TemporaryDirectory() as tmp:
            imagem, roteiro = self.preparar(Path(tmp))
            roteiro.write_text(json.dumps(roteiro_cores, ensure_ascii=False), encoding="utf-8")
            saida = caneta.anotar(roteiro)
            original, corrigida = tinta.carregar(imagem), tinta.carregar(saida)
            mudou = (original != corrigida).any(axis=-1)
            rotulos = tinta.classificar(corrigida)
            for (y0, y1), familia in [((60, 180), tinta.VERMELHO), ((280, 380), tinta.OUTRA), ((440, 600), tinta.VERDE)]:
                faixa = rotulos[y0:y1][mudou[y0:y1]]
                self.assertGreater(len(faixa), 100)
                self.assertGreater((faixa == familia).mean(), 0.9, tinta.NOMES[familia])

    def test_inventario_ignora_as_correcoes(self):
        with tempfile.TemporaryDirectory() as tmp:
            imagem, roteiro = self.preparar(Path(tmp))
            caneta.anotar(roteiro)
            caneta.grade(imagem)
            self.assertTrue((roteiro.parent / "6.grade.png").is_file())
            self.assertEqual(tinta.listar_imagens(imagem.parent), [imagem])

    def test_imagem_inexistente_e_roteiro_invalido(self):
        with tempfile.TemporaryDirectory() as tmp:
            imagem, roteiro = self.preparar(Path(tmp))
            outro = roteiro.with_name("7.json")
            outro.write_text(json.dumps(roteiro_valido()), encoding="utf-8")
            with self.assertRaises(FileNotFoundError):
                caneta.anotar(outro)
            roteiro.write_text(json.dumps({"marcas": [{"tipo": "x"}]}), encoding="utf-8")
            with self.assertRaises(ValueError):
                caneta.anotar(roteiro)


if __name__ == "__main__":
    unittest.main()
