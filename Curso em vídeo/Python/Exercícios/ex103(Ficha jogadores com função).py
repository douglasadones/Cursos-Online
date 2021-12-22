# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.
def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


# Programa Principal
print('-' * 20)
n = str(input('Nome do Jogador: ')).strip()
g = str(input('Número de Gols: ')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if len(n) == 0:
    ficha(gols=g)
else:
    ficha(n, g)

# Outras ideias de lógica dps da solicitação de dados:
'''
if len(n) != 0 and len(g) != 0:
    ficha(n, g)
elif len(n) == 0 and len(g) != 0:
    ficha(gols=g)
elif len(n) != 0 and len(g) == 0:
    ficha(jogador=n)
else:
    ficha()

Ou

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
'''
