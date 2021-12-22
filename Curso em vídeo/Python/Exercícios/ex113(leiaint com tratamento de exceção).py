# Reescreva a função leiaInt() do ex 104, incluindo agora a possibilidade da digitação de um número de tipo inválido
# Aproveire e crie também a uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(dado):
    while True:
        try:
            inteiro = str(input(dado))
            inteiro = int(inteiro)
        except KeyboardInterrupt:
            print('O Usuário preferiu não digitar esse número')
        except:
            print('\033[1;31mERRO: Por favor, digite número interio válido.\033[m')
        else:
            break
    return inteiro


def leiaFloat(dado):
    while True:
        try:
            real = str(input(dado)).strip().replace(',', '.')
            real = float(real)
        except KeyboardInterrupt:
            print('O Usuário preferiu não digitar esse número')
        except:
            print('\033[1;31mERRO: Por favor, digite um número real válido.\033[m')
        else:
            break
    return real


# Programa Principal
int = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {int} e o real foi {real}')
