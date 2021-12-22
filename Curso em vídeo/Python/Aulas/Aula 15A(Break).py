# loop infinito
cont = 1
'''while True: #loop infinito
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

# lendo um número:
n = s = 0
'''while n != 999: # flag
    n = int(input('Digit um número: '))
    s += n
print('A soma vale {}'.format(s))'''
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break # aqui ele não vai considerar o 999 na soma (já pula para fora do while (linha 20))
    s += n
print('A soma vale {}'.format(s))
print(f'A soma vale {s}') # novo método para intercalar entre str e variável (tudo formatado)