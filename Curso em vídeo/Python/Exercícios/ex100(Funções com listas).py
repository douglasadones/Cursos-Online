# Programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocálos dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.
from time import sleep
from random import randint
números = []


def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        sleep(0.5)
        n = randint(0, 10)
        números.append(n)
        print(n, end=' ')
    print('PRONTO!')


def somaPar():
    print(f'Somando os valores pares de {números}, temos', end=' ')
    soma = 0
    for c in números:
        if c % 2 == 0:
            soma += c
    print(soma)


sorteia()
somaPar()
