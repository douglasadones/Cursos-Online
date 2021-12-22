valores = []
#valores = list() Podemos criar uma lista dessa forma também.
valores.append(5)
valores.append(9)
valores.append(4)
print(valores) #mostra só que fica feião.

for v in valores: # Assim ele fica mais bonito
    print(v, end=' ')

for c, v in enumerate(valores): #Aqui nós podemos especificar a posição de cada elemento.
    print(f'\nNa posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
