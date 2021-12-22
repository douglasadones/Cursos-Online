#Programa que crie uma matriz de dimensões 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela com a formatação correta.
matriz = [[], [], []] #Guanabara fez assim: matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] e continuou igual abaixo.
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para {[l, c]}: ')))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print() #Quebra de linha para poder montar a matriz
