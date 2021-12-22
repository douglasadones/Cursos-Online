# Crie um programa que leia um valor em metros e os exiba convertidos em centímetros e milímetros.
n = float(input('Escreva um valor em metros: '))
print('A medida de {}m corresponde a'.format(n))
print('{}km'.format(n/1000))
print('{}hm'.format(n/100))
print('{}dam'.format(n/10))
print('{:.0f}dm'.format(n*10))
print('{:.0f}cm'.format(n*100))
print('{:.0f}mm'.format(n*1000))
