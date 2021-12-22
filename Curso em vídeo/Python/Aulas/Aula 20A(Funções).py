#Sem função
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

print()

#Com função:
def soma(a, b): #Definindo uma função para somar e mostar o resultado de forma mais rápida.
    print(f'A = {a}, B = {b}')
    s = a + b
    print(s)


#programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=20, b=40) #Podemos explicitar o parâmetro.
soma(b=20, a=40)

# Comportamentos que geram erros:
'''
soma(4) # Aqui daria ERRO pq nós definimos uma função que exige 2 parâmetros.
soma(b=5, 6) # Aqui também dá um ERRO pois a função espera a identificação explícita do outro parâmetro.
soma(4, 9, 2) # Aqui o ERRO seria pq existe mais parâmetros do que o definido pela função.
'''

# Quando não explicitamos, por padrão, os parâmetros serão recebidos de acordo com a ordem definida na função.