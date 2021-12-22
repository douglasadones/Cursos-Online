# Programa que leia um número inteiro e converta para binário, octal ou hexadecimal
numero = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] Converter para \033[1;34mBINÁRIO\033[m\n[ 2 ] Converter para \033[1;35mOCTAL\033[m
[ 3 ] Converter para \033[1;33mHEXADECIMAL\033[m''')
escolha = int(input('Sua opção:\n'))
if escolha == 1:
    # binario = bin(numero).split('b')
    print('O número {} em binário é \033[1;34m{}\033[m'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    # octal = oct(numero).split('o')
    print('O número {} em octal é \033[1;35m{}\033[m'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    # hexa = hex(numero).split('x')
    print('O número {} em hexadecimal é \033[1;33m{}\033[m'.format(numero, hex(numero)[2:]))
else:
    print('Digite um número inteiro entre 1 e 3')
