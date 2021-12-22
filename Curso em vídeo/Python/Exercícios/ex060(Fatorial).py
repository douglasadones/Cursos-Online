#Programa que leia um número e mostre o seu fatorial
n = int(input('Digite um número pra ver seu fatorial: '))
k = n + 1
cont = 1
print('\033[1;34m{}!\033[m'.format(n), end=' = ')
while k > 2:
    k = k - 1
    cont *= k
    print(k, end=' x ')
print('1 = \033[1;34m{}\033[m'.format(cont))

#Usando o laço for:
'''print('\033[1;34m{}!\033[m'.format(n), end='=')
for i in range(n, 1, -1):
    k = k - 1
    cont *= k
    print(k, end='x')
print('1=\033[1;34m{}\033[m'.format(cont))'''
