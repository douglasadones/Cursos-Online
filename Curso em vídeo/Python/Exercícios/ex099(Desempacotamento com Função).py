# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros. Seu progama te que analisar todos os valores e dizer qual deles é o maior.


def maior(* num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    maior = 0
    if len(num) == 1 and num[0] == 0:
        print('Foram informados 0 valores ao todo.')
    else:
        for pos, val in enumerate(num):
            if pos == 0:
                maior = val
            else:
                if val > maior:
                    maior = val
            print(val, end=' ')
        print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor foi {maior}.')


maior(5, 3, 4, 2, 8, 9, 10, 1)
maior(9, 8, 2)
maior(5, 9)
maior(5)
maior(0)
maior()

# ou eu poderia simplesmente usar a função max() pra descombrir qual é o maior. :D