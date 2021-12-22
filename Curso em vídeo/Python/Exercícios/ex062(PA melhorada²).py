n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 0 #controle que será zerado a cada repetição para garantir a quantidade solicitada do usuário
total = 0 # controle total dos termos
while not cont == 10:
    print('{}'.format(n), end='')
    n += r
    cont += 1
    total += 1
    print(' -> ' if cont < 10 else '.', end='')
cont = 0
escolha = int(input('\nMostrar mais quantos termo? '))
while escolha != 0:
    while cont != escolha:
        print('{}'.format(n), end='')
        n += r
        cont += 1
        print(' -> ' if cont < escolha else '.', end='')
        total += 1
    cont = 0
    escolha = int(input('\nMostrar mais quantos termo? '))
    if escolha == 0:
        print('Fim do programa. Foram mostrados {} termos.'.format(total))
