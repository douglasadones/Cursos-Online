#Programa que leia 2 valores e mostre um menu funcinal na tela''''''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('>>>>> Qual a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('O maior número entre {} e {} é {}.'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('O maior número entre {} e {} é {}.'.format(n1, n2, maior))
        else:
            print('Os dois números são iguais!')
    elif opção == 4:
        print('Informe os novo números.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-='*10)
print('Fim do programa. Volte sempre!')
