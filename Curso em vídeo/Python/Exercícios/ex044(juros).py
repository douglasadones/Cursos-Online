# Programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condições
# de pagamento.
preco = float(input('Informe o valor do produto: R$'))
print('Como deseja realizar o pagamento?')
pagamento = int(input('Digite \033[31m1\033[m para pagamento à vista ou \033[31m2\033[m para pagamento parcelado:\n'))
if pagamento == 1:
    print('informe a forma de pagamento: ')
    metodo = int(input('Digite \033[31m1\033[m para dinheiro/Cheque ou \033[31m2\033[m para à vista no cartão:\n'))
    if metodo == 1:
        preco = preco - (preco * (10 / 100))
        print('Você ganhou 10% de desconto! O valor do produto será de \033[34mR${:.2f}\033[m'.format(preco))
    elif metodo == 2:
        preco = preco - (preco * (5 / 100))
        print('Você ganhou 5% de desconto! O valor do produto será de \033[34mR${:.2f}\033[m'.format(preco))
    else:
        print('Escolha um método de pagamento válido.')
elif pagamento == 2:
    print('informe a forma de pagamento: ')
    parcelas = int(input('informe a quantidade de parcelas: entre \033[31m2\033[m e \033[31m12\033[m\n'))
    if parcelas == 2:
        print('O valor a ser pago será de \033[34mR${:.2f}\033[m'.format(preco))
    elif 3 <= parcelas <= 12:
        preco = preco + (preco * 20 / 100)
        print('Foram acrecidos 20% de juros. O valor do produto será de \033[34mR${:.2f}\033[m'.format(preco))
    else:
        print('Escolha um parcelamento válido.')
else:
    print('Digite uma forma de pagamento válida.')
