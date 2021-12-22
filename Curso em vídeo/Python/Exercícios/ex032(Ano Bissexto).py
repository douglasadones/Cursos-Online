ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0:
    if ano % 100 != 0:
        print('O ano {} é Bissexto!'.format(ano))
    else:
        if ano % 400 == 0:
            print('{}  É um ano bissexto!'.format(ano))
        else:
            print('{} não é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))
