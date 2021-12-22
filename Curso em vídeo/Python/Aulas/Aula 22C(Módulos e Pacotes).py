# Podemos criar pacotes contendo defs separadas por outros pacotes, melhorando a facilidade para encontrar uma
# determinada função. Para criar um pacote, devemos ir em new -> Python Package.
# (O Arquivo necessário __init__.py será criado automaticamente pelo pycharm). # A sintaxe para importar é a mesma.
from uteis import MA22 # (úteis é o pacote e o MA22 é o módulo ou o outro pacote dentro de úteis)

num = int(input('Digite um valor: '))
fat = MA22.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {MA22.dobro(num)}')
print(f'O triplo de {num} é {MA22.triplo(num)}')

from uteis.MA22 import fatorial, dobro, triplo # (Podemos importar com essa sintaxe para evitar o uso do "MA22.")

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')

# Aqui estou importando de dentro do pacote uteis outros dois pacotes internos

from uteis import novo, outro # De dentro do pacote uteis, importei o pacote "novo" e "outro".
novo.vermelho(5)
outro.azul(9)
