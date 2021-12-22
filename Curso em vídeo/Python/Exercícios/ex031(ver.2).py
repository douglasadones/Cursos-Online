d = float(input('Qual a distância da viagem em km? '))
# preço = d * 0.50 if d <= 200 else: d * 0.45  (poderia ser assim tbm. Método chamado de if line ou operador ternário)
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('O valor da viagem será de R${:.2f}'.format(preço))
