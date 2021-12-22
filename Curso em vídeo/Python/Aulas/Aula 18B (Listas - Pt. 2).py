galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] #Lista dentro de lista
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])

for p in galera:
    print(p) #todas as listas
print()
for p in galera:
    print(p[0]) #Só os nomes
print()
for p in galera:
    print(p[1]) #Só as idades
print()
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.') #print mais elaborado
