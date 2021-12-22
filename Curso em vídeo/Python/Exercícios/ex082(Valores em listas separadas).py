#Crie um programa que leia vários valores e no final, mostre a lista com todos os valores
#Mostre ou tra lista apenas com os valores pares e outra lista apenas com os valores ímpares.
todos = []
pares = [] # se fizer todos = pares = impares = [] vou estar fazendo uma ligação entre listas.
impares = []
while True:
    escolha = ' '
    todos.append(int(input('Digite um valor: ')))
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
for n in todos:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'A ista completa é {todos}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
