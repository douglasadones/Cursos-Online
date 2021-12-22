n = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        cont = cont + 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO Número {} ele foi dividido \033[33m{}\033[m vezes.'.format(n, cont))
if cont == 2:
    print('E por isso ele \033[1;34mÉ PRIMO!\033[m')
else:
    print('E por isso ele \033[1;31mNÃO É PRIMO!\033[m')
