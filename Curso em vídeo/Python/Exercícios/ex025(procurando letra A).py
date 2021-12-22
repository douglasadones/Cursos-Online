'''Faça um programa que leia uma frase no teclado e mostre:
quantas vezes aparece a letra 'a'
em que posição ela aparece pela primeira vez
em que posição ela aparece pela última vez'''

frase = str(input('Escreva uma frase qualquer: ')).strip().lower()
print('A letra "a" aparece {} vezes.'.format(frase.count('a')))
print('A primeira letra "a" apareceu na posição {}'.format(frase.find('a') + 1))
print('A última letra "a" apareceu na posição {}'.format(frase.rfind('a') + 1))  # O problem todo estava nesse 'r'find
