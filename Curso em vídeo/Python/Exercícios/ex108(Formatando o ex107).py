# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um
# Valor monetário formatado.
from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')

# Cuidado com as várias chamadas da biblioteca! lembre que no pacote ex107 existe também uma FUNÇÃO com o nome moeda.
# Acontece todas as vezes: "Da BIBLIOTECA moeda, use a FUNÇÃO moeda: moeda.moeda(...).
