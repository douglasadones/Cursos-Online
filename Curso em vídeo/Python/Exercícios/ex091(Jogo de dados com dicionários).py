# Progama onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
dic = {'jogador1': randint(1, 6),
       'jogador2': randint(1, 6),
       'jogador3': randint(1, 6),
       'jogador4': randint(1, 6)}
print('Valores Sorteados')
ranking = list()
for k, v in dic.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True) #O (1) indica que será organizado a partir da segunda key.
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)