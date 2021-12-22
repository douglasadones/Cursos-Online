import math      # aqui, toda a biblioteca math é importada
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))
print('A raiz quadrada de {} é {:.2f}'.format(num, math.ceil(raiz)))
print('A raiz quadrada de {} é {:.2f}'.format(num, math.floor(raiz)))
