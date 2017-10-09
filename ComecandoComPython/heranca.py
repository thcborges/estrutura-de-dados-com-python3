class Transporte:

    def __init__(self, nome, peso, preco):
        self.nome = nome
        self.peso = peso
        self.preco = preco

    # Não é uma boa prática em python
    # def getNome(self):
    #     return self.nome
    #
    # def getPeso(self):
    #     return self.peso
    #
    # def getPreco(self):
    #     return self.preco


class Carro(Transporte):

    def __init__(self, nome, peso, preco, preco_seguro):
        Transporte.__init__(self, nome, peso, preco)
        self.preco_seguro = preco_seguro


t = Transporte('Fusca', 500, 3278.56)
print(t.nome)
print(t.preco)

carro = Carro('Fusca', 300.78, 3500.00, 800)
print(carro.nome)
print(carro.peso)
print(carro.preco)
print(carro.preco_seguro)
