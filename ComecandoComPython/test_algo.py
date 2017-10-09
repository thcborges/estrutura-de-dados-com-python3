# Este arquivo não executa no ambiente virtual criado
# pois o pytest não está dispon;ivel ainda para o python 3.6


def fatorial(num):
    if num == 0:
        return 1
    return num * fatorial()(num - 1)


def eh_par(num):
    if num % 2 == 0:
        return True
    return False


def test_fatorial():
    assert fatorial(0) == 1


def test_eh_par():
    assert eh_par(10) == True
