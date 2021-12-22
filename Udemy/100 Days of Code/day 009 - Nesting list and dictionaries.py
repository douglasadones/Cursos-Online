diario_de_viagem = {
    'França': ['Paris', 'Lille', 'Dijon']
}
#Aninhando Dicionário em dicionário
diario_de_viagem = {
    'França': {'cidades_visitadas': ['Paris', 'Lille', 'Dijon'], 'total_de_visitantes': 13},
    'Alemanha': {'cidades_visitadas': ['Berlin', 'Hamburg', 'Stuttgart'], 'total_de_visitantes': 5}
}
print(diario_de_viagem['França']['cidades_visitadas'])

#Aninhando Dicionários em um lista
diario_de_viagem = [
    {'País': 'França',
     'cidades_visitadas': ['Paris', 'Lille', 'Dijon'],
     'total_de_visitantes': 13
     },
    {'País': 'Alemanha',
     'cidades_visitadas': ['Berlin', 'Hamburg', 'Stuttgart'],
     'total_de_visitantes': 5
     }
]
print(diario_de_viagem[0]['total_de_visitantes'])