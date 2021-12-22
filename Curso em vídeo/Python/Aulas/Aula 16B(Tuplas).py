lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

#ou
for cont in range(0, len(lanche)):
    print(cont)

#ou ainda - Mostrando os itens da tupla:
for cont in range(0, len(lanche)):
    print(lanche[cont])

#para fazer o terceiro modo imprimir como o primeiro:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
    