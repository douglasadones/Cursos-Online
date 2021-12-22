#Programa que gera 5 números aleatórios em uma tupla e depois mostre qual o maior e o menor número
from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
print('Os valores sorteados foram: ')
for n in numeros:
    print(f'{n} ', end=' ')
print(f'\nO maior número sorteado foi {max(numeros)}') #Importante lembrar da função max()
print(f'O menor número sorteado foi {min(numeros)}') # min()
