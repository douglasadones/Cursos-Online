# Programa que leia o peso de 5 pessoas e mostre o maior e menor peso.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o {}° peso: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido é {}Kg'.format(maior))
print('O menor peso lido é {}Kg'.format(menor))
