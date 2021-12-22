'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.'''
escolha = ''
n = cont = maior = menor = 0
k = n
while escolha in 'S':
    n = int(input('Digite um número: '))
    cont += 1
    k += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('''Dos {} número digitados:
O maior é {}
O menor é {}
A média entre eles é {}'''.format(cont, maior, menor, k / cont))
