# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.
aproveitamento = dict()
gols = []
cadastros = []
total = 0

#Solicitação de dados
while True:
    aproveitamento['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
    for c in range(0, partidas):
        n = int(input(f'Quantos gols na partida {c}? '))
        total += n
        gols.append(n)
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = total
    cadastros.append(aproveitamento.copy())
    gols.clear()
    total = 0
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 25)

# Parte Superior da tabela
print(f'Cod', end=' ')
for c in aproveitamento.keys():
    print(f'{c:<15}', end='')
print()
print('-' * 40)

# Informações dos jogadores na tabela
for v, c in enumerate(cadastros):
    print(f'{v:>3}', end=' ')
    for i in c.values():
        print(f'{str(i):<15}', end='') #Cuidado com esse detalhe! Especificou que é str para que n haja comflito com números
    print()
print('-' * 40)
while True:
    n = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    while n >= len(cadastros) and n != 999 or n < 0:
        print(f'ERRO! Não existe jogador com código {n}!')
        n = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if n == 999:
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {cadastros[n]["nome"]}')
        for partidas, gols in enumerate(cadastros[n]["gols"]):
            print(f'   => Na partida {partidas}, fez {gols} gols.')
        print('-' * 40)
print('<< VOLTE SEMPRE >>')