#Crie um programa que leia vários valores e guarde em uma lista, não adicione valores repetidos
#E no final mostre os valores em ordem crescente.
numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print('-='*20)
print(f'Você digitou os valores: {sorted(numeros)}')
