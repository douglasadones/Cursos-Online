# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do python, só
# que fazendo a validação para aceitar apenas um valor numérico.
def leiaint(dado):
    while True:
        info = str(input(dado))
        if info.isnumeric():
            info = int(info)
            break
        else:
            print('\033[1;31mERRO! Digite um número interio válido.\033[m')
    return info


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
