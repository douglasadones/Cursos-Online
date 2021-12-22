# Programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem.
n1 = int(input('Escreva um número inteiro qualquer: '))
n2 = int(input('Escreva um segundo número inteiro qualquer: '))
if n1 > n2:
    print('O \033[1;33mPrimeiro valor\033[m é \033[1;36mMaior\033[m')
elif n2 > n1:
    print('O \033[1;33msegundo valor\033[m é \033[1;36mMaior\033[m')
else:
    print('\033[1;33mNão existe\033[m valor maior, os dois são \033[1;36mIguais\033[m')
