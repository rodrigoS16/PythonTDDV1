import sys

class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    @property
    def lances(self):
        return self.__lances[:]

    # def avalia(self, leilao: "Espera um leilao"):   # chama-se annotations,
    # para dar uma dica do q o metodo espera receber

    def adiciona_lance(self, lance: Lance):

        if not self.__lances \
            or self.__lances[-1].usuario.nome != lance.usuario and self.__lances[-1].valor < lance.valor:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError("O mesmo usuario nao pode propror 2 lances seguidos e o valor deve ser maior q o lance anterior")
