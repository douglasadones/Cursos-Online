from random import randint


def adivinha():
    numero = randint(1, 100)
    print('''
                 _   _           _           _                                   
     /\         | | (_)         (_)         | |                                  
    /  \      __| |  _  __   __  _   _ __   | |__     ___                        
   / /\ \    / _` | | | \ \ / / | | | '_ \  | '_ \   / _ \                       
  / ____ \  | (_| | | |  \ V /  | | | | | | | | | | |  __/                       
 /_/    \_\  \__,_| |_|   \_/   |_| |_| |_| |_| |_|  \___|                       


                      __                                      _         _____    
                     /_/                                     | |    _  |  __ \   
   ___      _ __    _   _   _ __ ___     ___   _ __    ___   | |   (_) | |  | |  
  / _ \    | '_ \  | | | | | '_ ` _ \   / _ \ | '__|  / _ \  | |       | |  | |  
 | (_) |   | | | | | |_| | | | | | | | |  __/ | |    | (_) | |_|    _  | |__| |  
  \___/    |_| |_|  \__,_| |_| |_| |_|  \___| |_|     \___/  (_)   (_) |_____/   


''')
    print('Bem vindo ao Jogo de adivinhação de número!\nEstou pensando em um número entre 1 e 100.')
    print(f'Pssst, a resposta correta é {numero}')


    # Escolhendo a dificuldade
    while True:
        dificuldade = str(input('Escolha uma dificuldade. Digite "fácil" ou "difícil": ')).strip().lower()
        if dificuldade == '':
            print('Escolha uma dificuldade válida')
        elif dificuldade == 'facil' or dificuldade == 'fácil':
            chances = 10
            break
        elif dificuldade == 'dificil' or dificuldade == 'difícil':
            chances = 5
            break
        else:
            print('Escolha uma dificuldade válida')
    print(f'Você tem {chances} tentativas para descobrir qual o número!')


    # Jogando
    while chances > 0:


        #Pedindo um palpite
        while True:
            try:
                while True:
                    palpite = int(input('Tente adivinhar: '))
                    if 0 < palpite <= 100:
                        break
                    else:
                        print('Escolha um número entre 1 e 100!')
            except:
                print('Ocorreu um erro! tente novamente.')
            else:
                break


        #Verificando se a resposta está ou não correta
        if palpite == numero:
            return print(f'Você adivinhou! A resposta é {numero}')
        elif palpite > numero:
            print('menos...')
            chances -= 1
        else:
            print('mais...')
            chances -= 1
        if chances != 0:
            print(f'Ainda restam {chances} tentativas.')
    print('Perdeu! Todas as tentativas acabaram!')


adivinha()
