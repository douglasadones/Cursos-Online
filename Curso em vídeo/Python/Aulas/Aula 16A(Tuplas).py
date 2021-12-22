# Obs: () para Tuplas, [] para Listas e {} para Dicionários
#OBS 2: Tuplas são imutáveis!
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Doce') # assim
print(lanche)
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Doce' #ou assim(Pós att 3.5). Ambos são Tuplas.
print(lanche)
print(lanche[1]) # 2° elemento da tupla
print(lanche[1:]) #do elemento [1] até o final.
print(lanche[:2])
print(lanche[-2]) # penúltimo elemento da Tupla
print(lanche[1:3]) # apenas o elemento [1] e o elemento [2] da tupla (ignorando o elemento [3])
print(lanche[0::2]) # Vai do primeiro elemento até o último "pulando" de 2 em 2 elementos.
print(lanche[::-1]) # Do fim para o começo.


# lanche[1] = 'Refrigerante' #aqui daria um erro, pois as tuplas são imutáveis