from random import choice
A1 = input('Primeiro aluno: ')
A2 = input('Segundo aluno: ')
A3 = input('Terceiro aluno: ')
A4 = input('Quarto alunoo: ')
lista = [A1, A2, A3, A4]
print('O aluno sorteado é: {}!'.format(choice(lista)))
