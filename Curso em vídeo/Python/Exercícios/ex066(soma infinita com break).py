# Programa que some todos os números digitados menos o 999 sem usar gambiarras
s = cont = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma total dos {cont} números informados é: {s}')
