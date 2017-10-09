lista = [1, 2, 3]
a, b, c = lista

print(a, b, c)

tupla = (1, 2, 3)
a, b, c = tupla

print(a, b, c)

tupla2 = (1, 2, 3, 4)
a, _, _, b = tupla2
print(a, b)

nome = "Thiago Borges"
c1, c2, *_ = nome
print(c1, c2)


def func(x, y = 3):
    return x ** 2, y ** 2


r1, r2 = func(2, 3)
print(r1, r2)

r3, r4 = func(2)
print(r3, r4)
