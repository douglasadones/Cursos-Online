estado = dict()
brasil = list()
for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado) #Aqui não dá certo pois n realizamos uma cópia e sim um fatiamento.
print(brasil)
print()
for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado[:]) #Aqui dá um ERRO pq n podemos usar tecnicas de fatiamento em dicionários
print(brasil)
print()
for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #METODO CORRETO. O .copy() funciona para copiar um dicionário.
print(brasil)
