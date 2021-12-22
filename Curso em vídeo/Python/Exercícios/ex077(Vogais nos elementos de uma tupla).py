#Programa que leia uma tupla e mostre apenas as vogais de cada elemento (Aqui tem uma dica MUITO IMPORTANTE!)
palavras = 'macaco', 'Cachorro', 'sapato', 'mouse', 'Dark', 'Souls', 'Bloodborne', 'Chrono', 'Trigger'
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
#Aqui é muito importante perceber que a cada for usado, adentramos em um subindice. Ex:
#A Tupla palavras é composta por vários elementos. quando usamos o comando for pela primeira vez, não é mostrado a tupla completa
# o "p" são os índices dessa tupla (as palavras contidas nela), logo, já estamos em um índice da tupla.
# Ao usarmos novamente o for em cima do "p" (Das palavras) agora estamos trabalhando com os subindice das palavras(as letras).
