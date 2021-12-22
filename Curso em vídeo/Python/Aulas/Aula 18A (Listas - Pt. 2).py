teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste) #Uma lista.
galera = list()
galera.append(teste[:]) #se for galera.append(teste) seria uma ligação.
print(galera) #Uma lista dentro de outra lista.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)