# Programa que diga se uma frase qualquer é um palídromo
frase = input('Digite uma frase qualquer: ').upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

# ou, no lugar do for para pegar o inverso de uma frase, poderíamos fazer assim: frase[::-1]
