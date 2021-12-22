#mostrar de forma tabulada
compras = 'Macarrão', 5, 'Leite', 3, 'Frango', 12, 'Serial', 4, 'Arroz', 7, 'Feijao', 5, 'Suco', 2.50
print('-'*40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('-'*40)
for c in range(0, len(compras), 2):
    print('{:.<31}R$ {:>6.2f}'.format(compras[c], compras[c + 1]))
print('-'*40)
