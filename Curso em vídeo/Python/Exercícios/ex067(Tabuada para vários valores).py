# Gerador de tabuadas. Encerra quando o usuário informar um número negativo.
while True:
    cont = 1
    n = int(input('Voce deseja ver a tabuada de que número? \033[1;34m[Número negativo para encerrar]\033[m '))
    print('-' * 40)
    if n < 0:
        break
    while cont != 11:
        print(f'{n} x {cont:>2} = {n * cont}')
        cont += 1
    print('-' * 40)
print('Programa encerrado.')
