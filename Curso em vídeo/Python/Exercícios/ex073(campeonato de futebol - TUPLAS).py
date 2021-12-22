# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol
# Na ordem de colocação
tabela = ('Tabela campeonato brasileiro de futebol de 2021', 'Atlético-MG', 'Flamengo'
          'Bragantino', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Internacional' 
          'Athletico-PR', 'Fluminense', 'América-MG', 'Atlético-GO', 'Cuiabá', 'São Paulo',
          'Ceará', 'Juventude', 'Santos', 'Bahia', 'Sport', 'Grêmio', 'Chapecoense')
print('=-='*15)
print(f'Lista dos times do Brasileirão: {tabela}')
print('=-='*15)
print(f'Os cinco primeiros colocados são: {tabela[0:5]}')
print('=-='*15)
print(f'Os cinco últimos colocados são: {tabela[-4:]}') #ou poderia ser {tabela[15:]}
print('=-='*15)
print(f'Times em ordem alfabécia: {sorted(tabela)}')
print('=-='*15)
print(f'Na tabela, o time da \033[34mChapecoense\033[m está na {tabela.index("Chapecoense") + 1}ª posição.') # atenção para as aspas duplas.
print('=-='*15)
