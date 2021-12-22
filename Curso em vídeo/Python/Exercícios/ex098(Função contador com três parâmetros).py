# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
# e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1, b) de 10 até 0, de 2 em 2 e c) uma contagem personalizada.
from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    if p == 0:
        p = 1
    if i > f and p > 0:
        p *= -1
    if i < f and p < 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        while i <= f:
            sleep(0.5)
            print(i, end=' ')
            i += p
        print('FIM!')
    else:
        while i >= f:
            sleep(0.5)
            print(i, end=' ')
            i += p
        print('FIM!')


contador(0, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
