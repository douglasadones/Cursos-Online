def metade(total):
    m = total / 2
    return m


def dobro(total):
    d = total * 2
    return d


def aumentar(total, porcento=0):
    aum = total + (total * (porcento/100))
    return aum


def diminuir(total, porcento=0):
    dim = total - (total * (porcento/100))
    return dim


# Adição do exercício 108:


def moeda(formatado):
    m = f'R${formatado:.2f}'.replace('.', ',')
    return m
