import pygame
from emoji import emojize
frase1 = 'SISTEMA AUTODESTRUTIVO DE ENSINO'
frase2 = 'DESCUBRA AQUI SE VOCÊ CONTINUARÁ COMIGO!'
print(emojize(':broken_heart:'*25))
print('\033[1;30;41m{:^40}\033[m'.format(frase1))
print('\033[31;1m{:^40}\033[m'.format(frase2))
print(emojize(':broken_heart:'*25))
n1 = float(input('\033[31mInforme a sua primeira nota:\033[m '))
n2 = float(input('\033[31mInforme a sua segunda nota:\033[m '))
media = (n1 + n2) / 2
if media >= 7.0:
    print('Nhe... você está aprovado.')
elif 5.0 < media < 6.9:
    print('Aha! parece que você ficará por mais uns dias! mais sorte na \033[4;31mRECUPERAÇÃO\033[m!')
else:
    print('\033[7;30;41mKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK\033[m')
    pygame.mixer.init()
    pygame.mixer.music.load('media.mp3')
    pygame.mixer.music.play()
    input()
