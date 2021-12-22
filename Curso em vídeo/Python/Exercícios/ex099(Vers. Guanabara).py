def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor foi {maior}.')


maior(5, 3, 4, 2, 8, 9, 10, 1)
maior(9, 8, 2)
maior(5, 9)
maior(5)
maior(0)
maior()
