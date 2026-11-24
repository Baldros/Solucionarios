"""Testes da classificação da tinta por família de cor, com imagens sintéticas."""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tinta  # noqa: E402


def rotulo(cor):
    return int(tinta.classificar(np.array([[cor]], dtype=np.uint8))[0, 0])


def pagina_sintetica():
    """Duas linhas pretas, uma nota azul na margem da segunda e uma linha verde."""
    img = np.full((300, 400, 3), 255, np.uint8)
    img[20:36, 20:300] = (20, 20, 20)
    img[100:116, 20:280] = (20, 20, 20)
    img[100:116, 310:390] = (50, 50, 200)
    img[200:216, 40:200] = (40, 160, 60)
    return img


class TestFamilias(unittest.TestCase):
    def test_papel(self):
        for cor in [(255, 255, 255), (240, 240, 240), (250, 248, 252), (230, 230, 255)]:
            self.assertEqual(rotulo(cor), tinta.FUNDO, cor)

    def test_preto_inclui_o_traco_leve(self):
        # O traço com menos pressão parece cinza, mas é tinta preta; o ruído
        # de compressão num preto escuro também não vira cor.
        for cor in [(0, 0, 0), (30, 30, 40), (120, 120, 120), (190, 190, 195)]:
            self.assertEqual(rotulo(cor), tinta.PRETO, cor)

    def test_familia_azul(self):
        # Azul puro, anil, azul claro, borda suavizada sobre o papel e azul escuro.
        for cor in [(40, 40, 200), (90, 70, 210), (70, 110, 220), (200, 200, 245), (20, 20, 90)]:
            self.assertEqual(rotulo(cor), tinta.AZUL, cor)

    def test_familia_verde(self):
        for cor in [(40, 160, 60), (150, 210, 150), (60, 140, 120), (90, 170, 40)]:
            self.assertEqual(rotulo(cor), tinta.VERDE, cor)

    def test_outra_cor(self):
        for cor in [(200, 40, 40), (230, 150, 30), (200, 50, 200)]:
            self.assertEqual(rotulo(cor), tinta.OUTRA, cor)


class TestFaixas(unittest.TestCase):
    def test_linhas_e_nota_na_margem(self):
        resultado = tinta.faixas(tinta.classificar(pagina_sintetica()))
        self.assertEqual(len(resultado), 3)
        primeira, segunda, terceira = resultado
        self.assertEqual((primeira.y0, primeira.y1), (20, 35))
        self.assertFalse(primeira.mista())
        self.assertTrue(segunda.mista())
        self.assertIn(tinta.AZUL, segunda.alcance)
        x0, x1 = segunda.alcance[tinta.AZUL]
        self.assertGreater(x0, 75)
        self.assertLess(segunda.alcance[tinta.PRETO][1], 75)
        self.assertEqual([f for f, _ in tinta.presentes(terceira.contagens)], [tinta.VERDE])

    def test_ruido_nao_vira_faixa(self):
        img = np.full((200, 200, 3), 255, np.uint8)
        img[50:52, 50:52] = 0
        self.assertEqual(tinta.faixas(tinta.classificar(img)), [])


class TestVersoes(unittest.TestCase):
    def test_contencao(self):
        a = np.full((480, 640, 3), 255, np.uint8)
        a[50:70, 40:600] = 0
        a[150:170, 40:500] = 0
        b = a.copy()
        b[300:320, 40:400] = 0
        c = np.full_like(a, 255)
        c[400:420, 40:600] = 0
        c[250:270, 100:300] = 0
        ga, gb, gc = (tinta.grade(tinta.classificar(x)) for x in (a, b, c))
        self.assertGreaterEqual(tinta.contencao(ga, gb), tinta.CONTENCAO_MIN)
        self.assertLess(tinta.contencao(gb, ga), tinta.CONTENCAO_MIN)
        self.assertLess(tinta.contencao(ga, gc), 0.5)

    def test_inventario_aponta_versao_anterior(self):
        anterior = np.full((480, 640, 3), 255, np.uint8)
        anterior[50:70, 40:600] = 0
        continuada = anterior.copy()
        continuada[300:320, 40:400] = (50, 50, 200)
        with tempfile.TemporaryDirectory() as pasta:
            Image.fromarray(anterior).save(Path(pasta) / "1.png")
            Image.fromarray(continuada).save(Path(pasta) / "2.png")
            saida = io.StringIO()
            with contextlib.redirect_stdout(saida):
                tinta.cmd_inventario(Path(pasta), reducao=1)
        self.assertIn("1.png está contida em 2.png", saida.getvalue())
        self.assertIn("preto", saida.getvalue())
        self.assertIn("azul", saida.getvalue())


class TestArquivos(unittest.TestCase):
    def test_ordem_natural_e_pastas_ocultas(self):
        with tempfile.TemporaryDirectory() as pasta:
            raiz = Path(pasta)
            (raiz / "Restos").mkdir()
            (raiz / ".camadas").mkdir()
            for nome in ["10.png", "2.png", "1.png", "Restos/1.png", ".camadas/1.azul.png"]:
                Image.new("RGB", (4, 4), "white").save(raiz / nome)
            nomes = [p.relative_to(raiz).as_posix() for p in tinta.listar_imagens(raiz)]
        self.assertEqual(nomes, ["1.png", "2.png", "10.png", "Restos/1.png"])

    def test_transparencia_vira_papel(self):
        img = Image.new("RGBA", (10, 10), (0, 0, 0, 0))
        img.paste((0, 0, 0, 255), (2, 2, 5, 5))
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "t.png"
            img.save(caminho)
            rotulos = tinta.classificar(tinta.carregar(caminho))
        self.assertEqual(rotulos[0, 0], tinta.FUNDO)
        self.assertEqual(rotulos[3, 3], tinta.PRETO)

    def test_camadas_separam_as_familias(self):
        with tempfile.TemporaryDirectory() as pasta:
            origem = Path(pasta) / "p.png"
            Image.fromarray(pagina_sintetica()).save(origem)
            with contextlib.redirect_stdout(io.StringIO()):
                tinta.cmd_camadas([origem], Path(pasta) / "camadas", reducao=1)
            gerados = sorted(p.name for p in (Path(pasta) / "camadas").iterdir())
            azul = tinta.classificar(tinta.carregar(Path(pasta) / "camadas" / "p.azul.png"))
        self.assertEqual(gerados, ["p.azul.png", "p.preto.png", "p.verde.png"])
        self.assertEqual(set(np.unique(azul)), {tinta.FUNDO, tinta.AZUL})


if __name__ == "__main__":
    unittest.main()
