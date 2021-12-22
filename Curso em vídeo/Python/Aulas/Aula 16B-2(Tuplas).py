lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')
#Ou tbm podem fazer assim:

for pos, cont in enumerate(lanche):
    print(f'Eu vou comer {cont} na posição {pos}')
print('Comi pra caramba!')
