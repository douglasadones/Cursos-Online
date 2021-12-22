n1 = int(input('Escreva o primeiro número: '))
n2 = int(input('Escreva o segundo número: '))
n3 = int(input('Escreva o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('O maior número é {}'.format(n1), end = ' ')
else:
    if n2 > n1 and n2 > n3:
        print('O maior número é {}'.format(n2), end = ' ')
    else:
        print('O maior número é {}'.format(n3), end = ' ')
if n1 < n2 and n1 < n3:
    print('e o menor número é {}'.format(n1))
else:
    if n2 < n1 and n2 < n3:
        print('e o menor número é {}'.format(n2))
    else:
        print('e o menor número é {}'.format(n3))
