def fat(n):
    if n == 0:
        return 1
    return n * fat(n - 1)


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def pot(base, exp):
    if exp == 0:
        return 1
    return base * pot(base, exp - 1)


print(fat(5))
print(fib(17))
print(pot(2, 10))
