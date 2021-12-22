# Função que aceite todos os parâmetros digitados (empacotamento (*))

def contador(*num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print()

# ou
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print()

def soma(* valores):
    s = 0
    for c in valores:
        s += c
    print(f'Somando os valores {valores} temos {s}')


soma(4, 5)
soma(5, 3, 1, 2, 5)
soma(5)
