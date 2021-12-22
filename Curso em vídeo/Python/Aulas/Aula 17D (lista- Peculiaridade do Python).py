#Peculiaridade do python - Ligação entre listas
a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'lista B: {b}')
b[2] = 8 #Aqui modificamos apenas a lista b mas o python muda tanto a lista a como a b, as listas estão ligadas.
print(f'Lista A: {a}')
print(f'lista B: {b}')

b = a[:] #Aqui não é mais uma ligação. É uma cópia. Jogamos todos os valores de a em b.
b[2] = 9 #A modificação só vale agora para a lista b.
print(f'\nLista A: {a}')
print(f'lista B: {b}') # apenas a lista b foi modificada.
