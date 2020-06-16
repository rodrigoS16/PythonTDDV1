from src.leilao.dominio import Usuario, Leilao
import pytest

from src.leilao.excessoes import LanceInvalido


@pytest.fixture
def cria_usuario_vini():
    return Usuario('Vini', 100.0)

@pytest.fixture()
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_propor_lance(cria_usuario_vini,leilao):
    cria_usuario_vini.propoe_lance(leilao, 50.0)
    assert cria_usuario_vini.carteira == 50.0

def test_deve_permitir_propor_lance_quando_valor_e_menor_que_valor_carteira(cria_usuario_vini,leilao):
    cria_usuario_vini.propoe_lance(leilao, 1.0)

    assert cria_usuario_vini.carteira == 99.0

def test_deve_permitir_propor_lance_quando_valor_igual_ao_valor_carteira(cria_usuario_vini,leilao):
    cria_usuario_vini.propoe_lance(leilao, 100.0)

    assert cria_usuario_vini.carteira == 0.0

def test_nao_deve_permitir_propor_lance_com_valor_maior_carteira(cria_usuario_vini,leilao):
    with pytest.raises(LanceInvalido):
        cria_usuario_vini.propoe_lance(leilao, 200.0)
