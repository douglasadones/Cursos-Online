# Tupla que mostre o número digitado por extenso
vin = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
       'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
       'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis',
       'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 < n > 20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        print(f'Você digitou o número \033[1;34m{vin[n]}\033[m')
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('Programa finalizado.\nObrigado por utilizar o programa!')
