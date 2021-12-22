from math import radians, sin, cos, tan
a = float(input('Digite um ângulo qualquer: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('seno de {} = {:.2f}'.format(a, s))
print('Cosseno de {} = {:.2f}'.format(a, c))
print('Tangente de {} = {:.2f}'.format(a, t))
