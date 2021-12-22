# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
# Perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor
# da prestação mensal, sabendo que ela não pode exceder 30% do salárioou então o empréstimo será negado.
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Em quantos anos você irá pagar a casa? '))
prestação = casa / (12 * anos)
if prestação <= salario * (30 / 100):
    print('\033[1;32mPARABÉNS!!\033[m')
    print('O emprestimo foi aprovado! O valor mensal a ser pago será de \033[4mR${:.2f}\033[m'.format(prestação))
else:
    print('\033[1;31mNEGADO!!\033[m')
    print('Infelizmente o valor da taxa ultrapassou 30% do seu salário.\nEmpréstimo negado.')
