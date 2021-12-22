n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 0
while not cont == 10:
    print(n, end=' -> ')
    n += r
    cont += 1
print('ACABOU!')
