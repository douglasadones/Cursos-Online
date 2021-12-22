from random import choice
from time import sleep
jogador = str(input('Pedra, Papel, Tesoura! o que você escolhe?\n')).title().strip()
escolha = jogador.split()
lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista)
if jogador == '' or jogador.isspace() == True:
    print('Faça alguma escolha!')
elif jogador in 'Pedra Papel Tesoura':
    if len(escolha) != 1:
        print('Apenas uma escolha por vez!')
    else:
        print('JO')
        sleep(0.5)
        print('KEN')
        sleep(0.5)
        print('PÔ!!')
        if computador == 'Pedra':
            if jogador == 'Pedra':
                print('EMPATE!')
                print('Também escolhi Pedra!')
            elif jogador == 'Papel':
                print('GANHOU!')
                print('Escolhi Pedra :/')
            else:
                print('PERDEU!')
                print('Escolhi Pedra!!')
        elif computador == 'Papel':
            if jogador == 'Papel':
                print('EMPATE!')
                print('Também escolhi Papel!')
            elif jogador == 'Tesoura':
                print('GANHOU!')
                print('Escolhi Papel :/')
            else:
                print('PERDEU!')
                print('Escolhi Papel!!')
        else:
            if jogador == 'Tesoura':
                print('EMPATE!')
                print('Também escolhi Tesoura!')
            elif jogador == 'Pedra':
                print('GANHOU!')
                print('Escolhi Tesoura :/')
            else:
                print('PERDEU!')
                print('Escolhi Tesoura!!')
else:
    print('Faça uma escolha válida!')

'''Método interessante utilizado pelo Guanabara:
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('O computador escolheu {}'.format(itens[computador])) #Aqui o os números de 0 a 2 se transformam nos itens
e essa ideia tbm foi usada para a escolha do jogador'''
