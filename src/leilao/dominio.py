from src.leilao.excessoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira: float, leilao=None):
        self.__nome = nome
        self.__carteira = carteira
        self.__leilao = leilao

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, valor):
        if self._valor_eh_valido(valor):
            raise LanceInvalido('Não pode propror um lance com valor maior que o valor da carteira')

        lance = Lance(self, valor)
        leilao.adiciona_lance(lance)
        self.__carteira -= valor

    def _valor_eh_valido(self, valor):
        return not valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    # def avalia(self, leilao: "Espera um leilao"):   # chama-se annotations,
    # para dar uma dica do q o metodo espera receber

    def adiciona_lance(self, lance: Lance):

        if self._lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance)
                                          and self._valor_maior_lance_anterior(lance))

    def _usuarios_diferentes(self, lance: Lance):
        if self.__lances[-1].usuario.nome != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuário não pode dar dois lances seguidos")

    def _tem_lances(self):
        return self.__lances

    def _valor_maior_lance_anterior(self, lance: Lance):
        if self.__lances[-1].valor < lance.valor:
            return True
        raise LanceInvalido('O valor do lance deve ser maior que o lance anterior')
