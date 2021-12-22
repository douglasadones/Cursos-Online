# Programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
aproveitamento = dict()
gols = []
total = 0
aproveitamento['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
aproveitamento['gols'] = gols[:]
aproveitamento['total'] = sum(gols) # Função que soma todos os lementos de uma lista!!!!
print('-=' * 25)
print(aproveitamento)
print('-=' * 25)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 25)
print(f'O jogador {aproveitamento["nome"]} jogou {len(gols)} Partidas.')

# Pode ser assim:
for c in range(0, len(gols)):
    print(f'  => Na partida {c}, fez {aproveitamento["gols"][c]}', 'gols' if aproveitamento["gols"][c] != 1 else 'gol.')
print(f'Foi um total de {aproveitamento["total"]}', 'gols' if aproveitamento["total"] != 1 else 'gol.')

print()

# Ou assim tbm:
for i, v in enumerate(aproveitamento['gols']): #Assim pq é uma lista
    print(f'  => Na partida {i}, fez {v}', 'gols' if v != 1 else 'gol.')
print(f'Foi um total de {aproveitamento["total"]}', 'gols' if aproveitamento["total"] != 1 else 'gol.')
