# Faça um programa que tenha uma função chama área(), que receba as dimensões de um terreno retangular
#(Largura e Comprimento) e mostre a área do terro.
def área(larg, comp):
    s = larg * comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {s:.1f}m²')

print(' Controle de Terreno')
print('-' * 20)
#Programa Principal
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
