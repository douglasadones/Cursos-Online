# Faça um programa que leia 7 números e guarde em uma única lista que mantenha separados os
#valores pares e impares. No final, mostre os valores pares e impres em ordem crescente.
lista = [[], []]
for n in range(1, 8):
    k = int(input(f'Digite o {n}° valor: '))
    if k % 2 == 0:
        lista[0].append(k)
    else:
        lista[1].append(k)
lista[0].sort()
lista[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
