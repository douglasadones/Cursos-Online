# Programa que leia o primeiro termo e a razão de uma PA. No fina, mostre os 10 primeiros termos dessa
# Progressão
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
decimo = n + (10 - 1) * r
for c in range(n, decimo + r, r):
    print(c, end=' -> ')
print('ACABOU')
