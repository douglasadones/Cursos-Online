compras = 'Macarrão', 5, 'Leite', 3, 'Frango', 12, 'Serial', 4, 'Arroz', 7, 'Feijao', 5, 'Suco', 2.50
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(compras)):
    if pos % 2 == 0: #Aqui ele percebeu que os produtos estão em posições pares
        print(f'{compras[pos]:.<30}', end='')
    else: # e os preços em posições ímpares
        print(f'R${compras[pos]:>7.2f}')
print('-'*40)