#Faça um progama que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
#quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
#em uma lista composta.
from random import randint
from time import sleep
print('-'*42)
print(f'{"JOGA NA MEGA SENA":^42}')
print('-'*42)
jogos = list()
lista = list()
r = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= {"SORTEANDO 4 JOGOS"} -=-=-=')
for c in range(0, r):
    jogos.clear()
    print(f'Jogo {c+1}: ', end=' ')
    while len(jogos) != 6:
        n = randint(1, 60)
        if n not in jogos:
            jogos.append(n)
    jogos.sort()
    lista.append(jogos[:])
    print(lista[c])
    sleep(0.8)
print(f'-=-=-=-=-= {"< BOA SORTE! >"} -=-=-=-=-=')
