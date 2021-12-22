i = homens = Mm20 = 0
while True:
    print('-' * 35)
    print('       CADASTRE UMA PESSOA')
    print('-'*35)
    idade = int(input('Informe a idade: '))
    if idade >= 18:
        i += 1
    sexo = ' ' # aqui tem que ter um espaço para o programa entender
    while sexo not in 'MF':
        sexo = str(input('Iforme o Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 35)
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        Mm20 += 1
    escolha = ' ' # aqui tem que ter um espaço para o programa entender
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('==========FIM DO PROGRAMA ==========')
print(f'Total de pessoas com mais de 18 anos: {i}')
print(f'Ao todo temos {homens} homen(s) cadastrado(s).')
print(f'E temos {Mm20} mulher(ers) com menos de 20 anos.')
