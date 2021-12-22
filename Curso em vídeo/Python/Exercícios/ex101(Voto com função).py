# Programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retonando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


# Programa principal
print('-' * 23)
ano = int(input('Em que ano você nasceu? '))
voto(ano)
