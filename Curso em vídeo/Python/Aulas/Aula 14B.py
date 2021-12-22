'''for c in range(1, 5):
    n = int(input('Digite um número: '))
print('Fim')'''

n = 1
while n != 0: # 'Flag' (Ponto de parada)
    n = int(input('Digite um número: '))
print('Fim')

r = 'S'
while r == 'S': # 'Flag' (Ponto de parada)
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
print('Fim')
