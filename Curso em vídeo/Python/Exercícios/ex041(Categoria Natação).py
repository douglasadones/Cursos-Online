# A confederação de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade.
from datetime import date
frase = '----Saiba Qual a Sua Categoria!----'
print('\033[1;34m{:^35}\033[m'. format(frase))
nascimento = int(input('Informe aqui seu ano de nascimento:\n'))
categoria = ['MIRIM', 'INFANTIL', 'JUNIOR', 'SÊNIOR', 'MASTER']
idade = date.today().year - nascimento
if idade <= 9:
    print('Sua categoria atual é: \033[1;34m{}\033[m'.format(categoria[0]))
elif 10 <= idade <= 14:
    print('Sua categoria atual é: \033[1;34m{}\033[m'.format(categoria[1]))
elif 15 <= idade <= 19:
    print('Sua categoria atual é: \033[1;34m{}\033[m'.format(categoria[2]))
elif idade == 20:
    print('Sua categoria atual é: \033[1;34m{}\033[m'.format(categoria[3]))
else:
    print('Sua categoria atual é: \033[1;34m{}\033[m'.format(categoria[4]))
