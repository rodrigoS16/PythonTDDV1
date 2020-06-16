from collections import OrderedDict
from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):
    # outro padrao de nomenclatura:
    # test_quando_adicionados_em_orde_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance

    def list_cenarios(self,must_createOnlyOne: bool = False, cenarios_adicionais: list = []):
        if (must_createOnlyOne == True):
            cenarios = [("Gui", 100.0)]
        else:
            cenarios = [("Gui", 100.0), ("Yuri", 150.0)]
            cenarios.extend(cenarios_adicionais)
        return cenarios

    def criaCenario(self,
                    must_reverse: bool = False,
                    must_createOnlyOne: bool = False,
                    cenarios_adicionais: list = []):

        cenarios = self.list_cenarios(must_createOnlyOne,cenarios_adicionais)
        cenarios.sort(key=lambda tup: tup[1], reverse=must_reverse)
        self.leilao = Leilao("Celular")

        for key, value in cenarios:
            usuario = Usuario(key)
            lance = Lance(usuario, value)
            self.leilao.adiciona_lance(lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.criaCenario()
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_caso_o_lance_for_maior_q_anterior(self):
        with self.assertRaises(ValueError):
            self.criaCenario(True)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.criaCenario(False, True)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(100.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        self.criaCenario(cenarios_adicionais=[("Vini", 200.0)])

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # se o ultimo usuario for diferente, deve permitir propor um lance
    # se o ultimo usuario for igual, nao deve permitir propor o lance
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.criaCenario(False, True)
        quantidade_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_lances)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        self.criaCenario()
        quantidade_lances = len(self.leilao.lances)
        self.assertGreaterEqual(2, quantidade_lances)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        try:
            self.criaCenario()
            quantidade_lances_original = len(self.leilao.lances)
            tuples = self.leilao.lances[len(self.leilao.lances)-1]
            self.leilao.adiciona_lance(Lance(usuario=tuples.usuario.nome, valor=300.0))
            self.fail(msg="Não lancou excessão")
        except ValueError:
            quantidade_lances = len(self.leilao.lances)
            self.assertEqual(quantidade_lances_original, quantidade_lances)

    def test_deve_lancar_excessao_caso_nao_tenha_valueError(self):
        with self.assertRaises(ValueError):
            self.criaCenario()
            tuples = self.leilao.lances[-1]
            self.leilao.adiciona_lance(Lance(usuario=tuples.usuario.nome, valor=300.0))


