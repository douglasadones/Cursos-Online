#Programa que leia 2 valores e mostre um menu funcinal na tela''''''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = int(input('''Menu:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
escolha: '''))
while escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
    if escolha == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
        escolha = int(input('''Menu:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
escolha: '''))
    if escolha == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
        escolha = int(input('''Menu:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
escolha: '''))
    if escolha == 3:
        if n1 > n2:
            print('Entre {} e {}, o maior é {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {}, o maior é {}'.format(n1, n2, n2))
        escolha = int(input('''Menu:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
escolha: '''))
    if escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        escolha = int(input('''Menu:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
escolha: '''))
if escolha == 5:
    print('FIM')
else:
    print('Escolha inválida!')
