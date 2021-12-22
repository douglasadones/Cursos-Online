def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('O Usuário preferiu não digitar esse número')
        except:
            print('\033[1;31mERRO: Por favor, digite número interio válido.\033[m')
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção:\033[m ')
    return opc













'''def menu():
    opção = ''
    while opção != 3:
        from time import sleep
        print('-' * 50)
        print(f'{"MENU PRINCIPAL":^50}')
        print('-' * 50)
        print('1 - Ver pessoas cadastradas\n2 - Cadastrar nova Pessoa\n3 - Sair do Sistema')
        while True:
            try:
                opção = int(input('Sua Opção: '))
            except:
                print('\033[1;31mERRO: Porfavor, digite um número inteiro válido.\033[m')
            else:
                break
        if opção == 1:
            print('-' * 50)
            print(f'{"OPÇÃO 1":^50}')
            print('-' * 50)
            sleep(1)
        elif opção == 2:
            print('-' * 50)
            print(f'{"OPÇÃO 2":^50}')
            print('-' * 50)
            sleep(1)
        elif opção == 3:
            print('-' * 50)
            print(f'{"Saindo do sistema... Até logo!":^50}')
            print('-' * 50)
            break
        else:
            print('\033[1;31mERRO! Digite uma opção válida!\033[m')'''