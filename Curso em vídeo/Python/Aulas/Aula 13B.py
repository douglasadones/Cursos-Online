'''n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('Fim')'''

'''i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input(('Passo: ')))
for c in range(i, f + 1, p):
    print(c)
print('FIM')'''

'''for c in range(0, 5):
    n = int(input(('Digite um Número: ')))
print('Fim')'''

s = 0
for c in range(0, 5):
    n = int(input(('Digite um Número: ')))
    s = s + n
print('O Somatório de todos os valores foi de {}'.format(s))