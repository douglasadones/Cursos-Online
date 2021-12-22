barato = ' '
pbarato = cont = total = caro = 0
print('-' * 40)
print('{:^40}'.format('PYTHON SHOP'))
print('-' * 40)
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    cont += 1
    if preço > 1000:
        caro += 1
    if cont == 1 or preço < pbarato:
        barato = produto
        pbarato = preço
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('{:-^40}'.format('FINALIZADO'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi o(a) {barato} que custa R${pbarato:.2f}')
