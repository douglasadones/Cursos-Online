# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quanto você tem na carteira? R$'))
dolar = real/3.27
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))
