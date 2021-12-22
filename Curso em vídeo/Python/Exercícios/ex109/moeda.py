# Módulos feitos e usado pelo exercício 107
def metade(total, formatado=False):
    m = total / 2
    if formatado:
        return moeda(m)
    else:
        return m


def dobro(total, formatado=False):
    d = total * 2
    if formatado: # tbm podemos usar a sintaxe: return d if formatado is false else return moeda(d)
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
