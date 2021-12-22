# Docstrings é basicamente o tutorial de como usar uma def. Aqui, vms saber  como adicionar um
# doc/tutorial de uso para uma função criada por nós.

# Basta abrir três aspas duplas (no local mostrado) e dar enter.
# Tudo entre essas aspas fará parte da docstring da sua função.

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela:
    :param i: início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador) #olha a docstring ae!
