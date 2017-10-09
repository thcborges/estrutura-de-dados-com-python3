lista1 = [1, 2, 3]
lista2 = [5, 6, 7, 8, 9, 10]
lista3 = lista1 + lista2

print(lista1)
print(lista3)
lista3.pop()
print(lista3)
lista3.pop(1)
print(lista3)
lista3.pop(len(lista3) - 1)
print(lista3)
lista3.remove(3)
print(lista3)

num = 10
if num in lista3:
    print('elemento encontrado')
else:
    print('elemento não encontrado')
print(len(lista3))

for i in lista3:
    print(i)

t_lista = tuple(lista3)
print(t_lista)

lista3.append(10)
print(lista3)

lista3.insert(1, 14)
print(lista3)

lista3.insert(len(lista3), 17)
print(lista3)

lista3.sort()
print(lista3)

print(lista3[-1])
print(lista3[1:3])
print(lista3[::-1])
print(lista3[-2])
