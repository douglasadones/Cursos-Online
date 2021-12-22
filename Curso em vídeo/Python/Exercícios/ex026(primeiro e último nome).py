#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip().title()
lista = nome.split()
print('Seu primeiro nome é: {}.'.format(lista[0]))
print('Seu último nome é: {}'.format(lista[len(lista) - 1])) #Cuidado com essa linha
# print(lista[len(lista)]) entendi que aqui não dá certo pq a função len() conta a quatidade de caracteres +1, logo, sempre excede o tamanho da lista.
