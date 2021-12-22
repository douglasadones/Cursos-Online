#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
# Qual foi o maior e o menor valor e onde eles se encontram.
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-='*20)
maior = max(valores)
menor = min(valores)
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor é {maior} e está na posição:', end=' ')
for v, c in enumerate(valores):
    if c == maior:
        print(f'{v}...', end=' ')
print(f'\nO menor valor é {menor} e está na posição:', end=' ')
for v, c in enumerate(valores):
    if c == menor:
        print(f'{v}...', end=' ')
