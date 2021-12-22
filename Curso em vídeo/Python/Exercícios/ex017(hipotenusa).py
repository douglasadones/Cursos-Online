# programa que peça o cateto oposto e adjacente de um triângulo retângulo e mostre o comprimento da hipotenusa.
from math import hypot, sqrt
Co = float(input('Cateto oposto: '))
Ca = float(input('Cateto adjacente: '))
h = hypot(Ca, Co)
# hp = sqrt(Ca**2 + Co**2)
print('A hipotenusa de um triangulo retângulo de catetos {} e {} é {}.'.format(Co, Ca, h))
