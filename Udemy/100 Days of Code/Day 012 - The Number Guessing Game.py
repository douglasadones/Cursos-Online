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
    dificuldade = str(input('Escolha uma dificuldade. Digite "fácil" ou "dificil": ')).strip().lower()
    if dificuldade in 'facilfácil':
        chances = 5
    else:
        chances = 10
    print(f'Você tem {chances} tentativas para descobrir qual o número!')
    while chances > 0:
        palpite = int(input('Tente adivinhar: '))
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
