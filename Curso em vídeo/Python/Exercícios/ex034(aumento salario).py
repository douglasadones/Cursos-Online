salario = float(input('Digite o valor do seu salário: R$'))
if salario > 1250:
    print('Seu salário com 10% de aumento é R${:.2f}'.format(salario * 1.1))
else:
    print('Seu salário com 15% de aumento é R${:.2f}'.format(salario * 1.15))
