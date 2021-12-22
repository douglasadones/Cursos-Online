# Programa que leia o ano de nascimento de um jovem e informe, sobre sua data de alistamento.
from datetime import date
data = date.today().year
print('-='*25)
print('\033[31mSAIBA AQUI SE VOCÊ ESTÁ NO PERÍODO DE ALISTAMENTO\033[m')
print('-='*25)
nascimento = int(input('Informe seu ano de nascimento: '))
idade = data - nascimento
if idade < 18:
    faltam = 18 - idade
    if faltam != 1:
        print('Você ainda não atingiu  18 anos. Faltam {} anos para você realizar seu alistamento.'.format(faltam))
    else:
        print('Você ainda não atingiu  18 anos. Próximo ano você deverá realizar seu alistamento.')
elif idade > 18:
    excedeu = idade - 18
    if excedeu != 1:
        print('Você excedeu o perído máximo de alistamento em {} anos.'.format(excedeu))
    else:
        print('Você excedeu o perído máximo de alistamento em 1 ano.')
else:
    print('Vocês está na data correta para realizar o seu alistamento.')
