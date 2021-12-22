from random import choice
import os
clear = lambda: os.system('cls')
clear()


def valor_as(jogador): # Verifica qual o valor da carta Ás.
    if 11 in jogador and sum(jogador) > 21:
        jogador[jogador.index(11)] = 1


print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
while True:
    # Primeiras Cartas de ambos os jogadores
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_jogador = [choice(cards), choice(cards)]
    cards_computador = [choice(cards), choice(cards)]


    # Verificando o valor do Às.
    valor_as(cards_jogador)
    valor_as(cards_computador)


    # Verificando se alguém ganhou na primeira partida
    if sum(cards_jogador) != 21 and sum(cards_computador) != 21:
        while sum(cards_jogador) < 21 and sum(cards_computador) < 21:
                print(f'Suas cartas: {cards_jogador}, pontuação atual: {sum(cards_jogador)}')
                print(f'Primeira carta do computador: {cards_computador[0]}')
                escolha = str(input('Digite "S" para pegar outra carta ou "N" para passar a vez: ')).strip().upper()[0]
                if escolha == 'S':
                    cards_jogador.append(choice(cards))
                    cards_computador.append(choice(cards))
                    valor_as(cards_jogador)
                    valor_as(cards_computador)
                else:
                    if sum(cards_computador) < 17:
                        cards_computador.append(choice(cards))
                        valor_as(cards_computador)
                    break

    #Verificando resultado final
    if sum(cards_computador) < sum(cards_jogador) <= 21 or sum(cards_computador) > 21:
        print(f'Suas cartas finais: {cards_jogador}, Pontuação final: {sum(cards_jogador)}')
        print(f'Cartas finais do computador: {cards_computador}, pontuação final: {sum(cards_computador)}')
        print('VENCEU!')
        if len(cards_jogador) == 2 and sum(cards_jogador) == 21:
            print('BLACKJACK!!')
    elif sum(cards_jogador) < sum(cards_computador) <= 21 or sum(cards_jogador) > 21:
        print(f'Suas cartas finais: {cards_jogador}, Pontuação final: {sum(cards_jogador)}')
        print(f'Cartas finais do computador: {cards_computador}, pontuação final: {sum(cards_computador)}')
        print('PERDEU!')
        if len(cards_computador) == 2 and sum(cards_computador) == 21:
            print('BLACKJACK!!')
    else:
        print(f'Suas cartas finais: {cards_jogador}, Pontuação final: {sum(cards_jogador)}')
        print(f'Cartas finais do computador: {cards_computador}, pontuação final: {sum(cards_computador)}')
        print('EMPATE!')

    repetir = str(input('Deseja jogar novamente? [S/N] ')).strip().upper()[0]
    if repetir == 'N':
        break
print('Obrigado por jogar!')
