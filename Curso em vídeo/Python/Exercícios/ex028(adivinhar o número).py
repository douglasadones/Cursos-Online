from random import choice
from time import sleep
print('***' * 20)
print('Estou pensando em um número entre 0 e 5! tente adivinhar... ')
print('***' * 20)
v = int(input(('Em que número estou pensando? ')))
print('Processando...')
sleep(3)
lista = [0, 1, 2, 3, 4, 5]
n = choice(lista)
print('Escolhi o número {}.'.format(n))
if v == n:
    print('Você adivinhou! PARABÉNS!')
else:
    print('Ganhei! Você ERROU!')
