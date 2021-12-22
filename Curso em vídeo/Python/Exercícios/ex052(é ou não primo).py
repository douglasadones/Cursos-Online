# Programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número inteiro: '))
for c in range(2, n):
    s = n % c
    if s == 0:
       n = 0
if n == 0 or n == 1:
    print('Não é um número primo!')
else:
    print('É um número primo!')
