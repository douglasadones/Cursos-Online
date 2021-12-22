# Lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela dada.
frase = 'CALCULADORA DE IMC'
print('{:^28}'.format(frase))
peso = float(input('Informe o seu peso em kg: '))
altura = float(input('Informe a sua altura em cm: '))
imc = (peso) / altura**2
if imc < 18.5:
    print('Seu IMC é {:.1f} e seu status é: \033[1;34mAbaixo do Peso\033[m'.format(imc))
elif 18.5 < imc < 25:
    print('Seu IMC é {:.1f} e seu status é: \033[1;34mPeso Ideal\033[m'.format(imc))
elif 25 <= imc <= 30:
    print('Seu IMC é {:.1f} e seu status é: \033[1;34mSobrepeso\033[m'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.1f} e seu status é: \033[1;34mObesidade\033[m'.format(imc))
else:
    print('Seu IMC é {:.1f} e seu status é: \033[1;34mObesidade Mórbida\033[m'.format(imc))
