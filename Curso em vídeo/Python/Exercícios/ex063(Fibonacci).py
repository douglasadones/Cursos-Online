cont = 2
k = 1
ant = 1
antdant = 1
elementos = int(input('Mostrar quantos elementos da sequência fibonacci? '))
print('{} -> {} -> '.format(0, 1), end='')
while cont < elementos:
    cont += 1
    print(k, end='')
    k = ant + antdant
    antdant = ant
    ant = k
    print(' -> ' if cont < elementos else '.', end='')
