# Programa que tenha uma função fatorial() que receba dois parâmetros: O primeiro que indique um número a calcular
# e o outro chamado show, que será um valor lógico (opcional) indicando se será motrado ou não na tela o processo de
# cálculo do fatorial


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um numero n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f # Note que se o "return f" for retirado, aparecerá o "none" no print, pois não há retorno.


# Programa principal
print(fatorial(6, True))
help(fatorial)
