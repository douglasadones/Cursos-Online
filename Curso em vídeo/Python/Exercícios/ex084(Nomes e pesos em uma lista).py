# Faça um progama que leia o nome e o peso de várias pessoas, guardando tudo em uma lista.
#Depois mostre: Quantas pessoas foram cadastradas, Uma lista com as pessoas mais pesadas
#E Uma lista com as pessoas mais leves.
r = ' '
dados = list()
cadastros = list()
maiorp = menorp = 0
while True:
    r = ' '
    dados.append(str(input('Nome: ')))
    dados.append(int(input('peso: ')))
    if len(cadastros) == 0:
        maiorp = menorp = dados[1]
    else:
        if dados[1] > maiorp:
            maiorp = dados[1]
        if dados[1] < menorp:
            menorp = dados[1]
    cadastros.append(dados[:])
    dados.clear()
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(cadastros)} pessoas.')
print(f'O maior peso foi de {maiorp:.1f}Kg. Peso de', end=' ')
for p in cadastros:
    if p[1] == maiorp:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menorp:.1f}Kg. Peso de', end=' ')
for p in cadastros:
    if p[1] == menorp:
        print(f'[{p[0]}]', end=' ')
