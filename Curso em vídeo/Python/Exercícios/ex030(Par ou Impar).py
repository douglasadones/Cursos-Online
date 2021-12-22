numero = int(input('Digite um número inteiro qualquer: '))
resto = numero % 2
if resto == 0:
    print('O número {} é PAR!'.format(numero))
else:
    print('O número {} é impar!'.format(numero))
