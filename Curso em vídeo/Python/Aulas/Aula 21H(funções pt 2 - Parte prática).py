# Criando uma fução  que dê o fatorial de um número.
'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
print()

# ou
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(3)
print(f'Os resultados são {f1}, {f2} e {f3}')'''


# O return não está limitado à números, pode retornar valores lógicos, listar, tuplas e etc... ex:
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))
# ou ainda
if par(num):
    print('É Par!')
else:
    print('Não é Par!')
