#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit (e kelvin).
C = float(input('Informe a temperatura em °C: '))
F = 9 * C / 5 + 32
K = C + 273
print('A temperatura de {}°C corresponde a {}°F e {}K.'.format(C, F, K))
