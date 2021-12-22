# Programa que mostre na tela uma contagem regressiva para o estou de fogos de artifício, indo
# de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('Contagem regressiva FOGOS DE ARTIFÍCIO!')
input('Aperte enter para iniciar a contagem!')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
