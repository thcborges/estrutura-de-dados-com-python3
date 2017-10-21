class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def add_aresta(self, u, v):
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1

    def show(self):
        for i in self.grafo:
            for j in i:
                print(j, end=', ')
            print()

    def tem_ligacao(self, u, v):
        if self.grafo[u - 1][v - 1] == 1:
            return True
        return False


g = Grafo(5)
g.add_aresta(1, 3)
g.add_aresta(3, 4)
g.add_aresta(2, 3)
g.add_aresta(3, 5)
g.add_aresta(4, 5)
g.show()

print(g.tem_ligacao(1, 5))
print(g.tem_ligacao(1, 3))
