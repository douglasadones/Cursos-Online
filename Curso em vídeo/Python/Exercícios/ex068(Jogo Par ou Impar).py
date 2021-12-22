# programa que jogue Ímapar ou Par com o jogador usando o comando break.
from random import randint
cont = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = jogador + computador
    if escolha not in 'PI':
        print('Opção Inválida.')
    else:
        print(f'Você jogou {jogador} e o computador {computador}. A soma é {soma}', end=' ')
        print('DEU PAR!' if soma % 2 == 0 else 'DEU IMPAR!')
        if escolha == 'P' and soma % 2 == 0 or escolha == 'I' and soma % 2 != 0:
            print('\033[1;34mVocê Ganhou!\033[m')
            cont += 1
        else:
            break
        print('Vamos tentar novamente...')
print(f'\033[1;31mGAME OVER!\033[m Você venceu {cont}', 'vez.' if cont == 1 else 'vezes.')
