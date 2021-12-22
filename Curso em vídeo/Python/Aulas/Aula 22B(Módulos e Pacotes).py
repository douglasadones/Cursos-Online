# Note que nós importamos o módulo que criamos e adicionamos no mesmo diretório desse arquivo.
import MA22

num = int(input('Digite um valor: '))
fat = MA22.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {MA22.dobro(num)}')
print(f'O triplo de {num} é {MA22.triplo(num)}')

# Também podemos importar códigos específicos como já foi feito. Ex: from MA22 import fatorial, dobro, triplo
# A ventagem desse modo é que não precisamos usar MA22. antes da função.

# O principal objetivo dos módulos é simplificar e legibilizar códigos muito grandes, remanejando as várias linhas
# destinadas à defs para um outro arquivo separado (módulo).

# Também podemos por esse módulo que criamos dentro de uma pasta para melhorar a organização. Basta, no mesmo diretório
# do arquivo principal, ir em new -> Directory e criar ou jogar o módulo para dentro da pasta. Nesse caso, para poder
# importar, a sintaxe é a seguinte: from (nome do Directory) import MA22 ou também podemos usar a
# sintaxe: from (nome do Directory).MA22 import fatorial, dobro, triplo. Para evitar o uso, por exemplo, da chamada
# MA22.fatorial(), sendo necessário somente fatorial().
