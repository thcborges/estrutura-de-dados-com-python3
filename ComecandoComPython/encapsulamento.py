class Pessoa:

    def __init__(self):
        self.__nome = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

p = Pessoa()
p.nome = 'Thiago'
print(p.nome)
