#Programa que crie uma matriz de dimensões 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela com a formatação correta e as seguintes informações:
#A soma de todos os valores pares digitados, A soma de todos os valores da terceira coluna
# E o maior valor da segunda coluna.
matriz = [[], [], []]
somapar = tercoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        k = int(input(f'Digite um valor para {[l, c]}: '))
        matriz[l].append(k)
        if k % 2 == 0:
            somapar += k
        if c == 2:
            tercoluna += k
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {tercoluna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
