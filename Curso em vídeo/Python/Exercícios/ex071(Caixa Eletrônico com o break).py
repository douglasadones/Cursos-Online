#considerando que o caixa possúa cédulas de R$50, R$ 20, R$10 e R$ 1.
valor = int(input('Digite o valor a ser sacado: R$'))
total = valor
céd = 50
totcéd = 0
print('=' * 30)
print('{:^30}'.format('BANCO PYTHON'))
print('=' * 30)
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('{:^30}'.format('Volte sempre ao BANCO PYTHON'))
print('{:^30}'.format('Tenha um bom dia!'))
