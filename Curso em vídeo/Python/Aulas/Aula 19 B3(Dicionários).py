estado = dict()
brasil = list()
for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # METODO CORRETO. O .copy() funciona para copiar um dicionário.
for e in brasil: #Referente a lista
    print(e) #Cada estado é um diocionário.

for e in brasil: #Referente a lista
    for k, v in e.items(): #Referente ao Dicionário
        print(f'O Campo {k} tem o valor {v}')

for e in brasil: #Referente a lista
    for v in e.values(): #Referente ao Dicionário
        print(v, end=' ')
    print()