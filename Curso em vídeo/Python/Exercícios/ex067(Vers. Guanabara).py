while True:
    n = int(input('Voce deseja ver a tabuada de que número? \033[1;34m[Número negativo para encerrar]\033[m '))
    print('-' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:>2} = {n * c}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
