import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('\033[1;34mBem vindo ao gerador de senhas!')
num_letras = int(input('Quantas letras você deseja em sua senha?\n'))
num_simbolos = int(input(f'Quantos símbolos?\n'))
num_numeros = int(input(f'Quantos números?\n'))

lista_da_senha = []

for caractere in range(1, num_letras + 1):
    lista_da_senha.append(random.choice(letras))

for caractere in range(1, num_simbolos + 1):
    lista_da_senha += random.choice(simbolos)

for caractere in range(1, num_numeros + 1):
    lista_da_senha += random.choice(numeros)

random.shuffle(lista_da_senha)

senha = ''
for caractere in lista_da_senha:
    senha += caractere

print(f'Sua senha é:\033[m \033[1;31m{senha}\033[m')
