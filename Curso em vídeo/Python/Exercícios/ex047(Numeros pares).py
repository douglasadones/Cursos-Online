# programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50.
print('Números pares no intervalo de 1 a 50: ')
for n in range(1, 51): # se a gente por para imprimir um ponto, vai ver que o programa faz vários laços procurando os numeros pares.
    #print('.', end=' ')
    if n % 2 == 0:
        print(n, end=' ')

# ou faz assim:
for n in range(2, 51, 2): # aqui, o programa é mais limpo/leve ele vai direto nos numeros pares
    print(n, end=' ')
