# Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira.
'''from math import trunc
n = float(input('Digite um número real qualquer: '))
i = trunc(n)
print('A parte inteira de {} é {}.'.format(n,i))'''

n = float(input('Digite um número qualquer: '))
print('A parte inteira do número {} é {}.'.format(n, int(n)))
