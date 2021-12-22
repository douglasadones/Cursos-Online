# Módulo usado pelo exercício 107
def metade(total, formatado=False):
    m = total / 2
    if formatado:
        return moeda(m)
    else:
        return m


def dobro(total, formatado=False):
    d = total * 2
    if formatado:
        return moeda(d)
    else:
        return d


def aumentar(total, porcento=0, formatado=False):
    aum = total + (total * (porcento/100))
    if formatado:
        return moeda(aum)
    else:
        return aum


def diminuir(total, porcento=0, formatado=False):
    dim = total - (total * (porcento/100))
    if formatado:
        return moeda(dim)
    else:
        return dim


# Adição do exercício 108:


def moeda(formatado):
    m = f'R${formatado:.2f}'.replace('.', ',')
    return m


# Obs: O Parâmetro opcional "formatado=False" foi uma adição do exercício 109 para dexar o exercício 108 mais organizado

# Obs2: A Função resumo() é uma adição do exercício 110.


def resumo(total, aum=5, dim=10):
    print(f'-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print(f'-' * 30)
    aumento = f'{aum}% de aumento:'
    redução = f'{dim}% de redução:'
    print(f'Preço analizado: \t{moeda(total)}')
    print(f'Dobro do preço: \t{dobro(total, True)}')
    print(f'Metade do preço: \t{metade(total, True)}')
    print(f'{aumento} \t{aumentar(total, aum, True)}')
    print(f'{redução} \t{diminuir(total, dim, True)}')
    print(f'-' * 30)
