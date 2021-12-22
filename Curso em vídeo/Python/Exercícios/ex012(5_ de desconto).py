# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Digite o preço do produto: R$'))
novo = preço * 0.95
print('O Valor do produto com 5% de desconto é R$ {:.2f}'.format(novo))
