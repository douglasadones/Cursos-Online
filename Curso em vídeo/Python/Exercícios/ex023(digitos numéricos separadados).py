#Faça um programa que leia um número entre 0 e 9999 e mostre cada um dos dígitos separados (unidade, dezena, centena e milhar)
numero = int(input('Digite um número qualquer entre 0 e 9999: '))
u = numero % 10
d = numero % 100 // 10 #note que "%" elimina os números à esquerda do número desejado e "//" elimina os números à direita do número desejado.
c = numero % 1000 // 100
m = numero % 10000 // 1000
print("aaaa: $c")
print('Unidade: {}'.format(u))
print('Dezena: {}'. format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

''' Ou poderia ser assim:
   u = numero // 1 % 10 
   d = numero // 100 % 10
   c = numero // 1000 % 10
   m = numero // 10000 % 10'''
