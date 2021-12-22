#Programa que leia um número e mostre o seu fatorial
n = int(input('Digite um número pra ver seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='') # olha essa sacada!
    f *= c # Atenção na ordem!
    c -= 1
print('{}'.format(f))
