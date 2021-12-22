galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Se aqui fosse uma ligação, p .clear() limparia tanto "dado" como "galera".
    dado.clear()
print(galera)
print()
totmai = totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é Maior de idade.') #Mostrando apenas os maiores de idade
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.') #Mostrando apenas os menores de idade
        totmen += 1
print(f'Temos {totmai} Maiores e {totmen} menores de idade.')
