# Faça um minisistema que utilize o interactive help do python. O usuário vai digitar o comando e o maual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
def ithelp(escolha):
    while True:
        from time import sleep
        # Título
        txt = 'SISTEMA DE AJUDA PyHELP'
        tam = len(txt) + 4
        print('\033[42m')
        print('~' * tam)
        print(f'  {txt}')
        print('~' * tam)
        print('\033[m')
        sleep(0.5)

        # Solicitação de dado
        dado = str(input(escolha)).strip()
        sleep(0.5)
        if dado.upper() in 'FIM':
            txt = '  ATÉ LOGO'
            tam = len(txt) + 4
            print('\033[41m')
            print('~' * tam)
            print(f'  {txt}')
            print('~' * tam)
            print('\033[m')
            sleep(0.5)
            break

        # Título para mostrar dados
        txt2 = f'  Acessando o manual do comando "{dado}"  '
        tam2 = len(txt2) + 4
        print('\033[44m')
        print('~' * tam2)
        print(f'  {txt2}')
        print('~' * tam2)
        print('\033[m')
        sleep(1)

        # Mostrando dados
        print('\033[7;40m')
        help(dado)
        print('\033[m')
        sleep(2)


ithelp('Função ou Biblioteca > ')
