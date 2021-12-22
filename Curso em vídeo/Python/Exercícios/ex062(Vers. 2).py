n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
primeiro = n
cont = 1
total = 0
escolha = 10
while escolha != 0:
    total += escolha
    while cont <= total:
        print('{} -> '.format(primeiro), end='')
        primeiro += r
        cont += 1
    print('PAUSA')
    escolha = int(input('Mostrar mais quantos termo? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
