# Programa que calcule a soma entre todos os numeros primos que são múltiplos de três que se encontram
# no intervalo de 1 até 500.
s = 0 #acumulador
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s = s + c
print('A soma dos números primos múltiplos de 3 entre 1 e 500 é {}'.format(s))

#ou faz assim:
soma = 0 #acumulador
cont = 0 #contador
for c in range(1, 501, 2): #Aqui já tem apenas os números ímpares.
    if c % 3 == 0:
        cont = cont + 1 # no python, poderia ser: cont += c
        soma = soma + c # no python, poderia ser: soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))