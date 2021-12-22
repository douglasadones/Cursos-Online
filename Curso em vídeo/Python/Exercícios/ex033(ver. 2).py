n1 = int(input('Escreva o primeiro número: '))
n2 = int(input('Escreva o segundo número: '))
n3 = int(input('Escreva o terceiro número: '))
lista = [n1, n2, n3]
crescente = sorted(lista)
print('O maior número é {} e o menor número é {}'.format(crescente[2], crescente[0]))
