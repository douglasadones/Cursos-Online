#Programa que leia vários números e depois diga: quantos números foram digitados,
# ordene de forma decrescente e informe se o número 5 está na lista.
num = []
while True:
    escolha = ' '
    num.append(int(input('Digite um valor: ')))
    num.sort(reverse=True)
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Você digitou {len(num)} elementos.')
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print(f'O valor 5 faz parte da lista! e está na posição {num.index(5)+1}')
else:
    print('O valor 5 não faz parte da lista!')
