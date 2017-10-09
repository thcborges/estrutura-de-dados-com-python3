import random


print(random.randrange(10))  # retorna números inteiros entre 0 e 9

print(random.randint(1, 4))  # retorna números inteiros entre 1 e 4

# Algumas formas de se criar uma lista
# lita = [i for i in range(10)]
# li = list(range(10))

lista = [i for i in range(10)]
print(random.choice(lista))  # retorna um número da lista
random.shuffle(lista)  # embaralha a sequencia
print(lista)

print(random.sample(lista, 3))  # retorna uma lista com 3 números da lista passada

print(random.random())  # retorna um valor entre 0 e 1 exclusivo

print(random.uniform(1, 10))  # retorna um valor entre 1 e 10
