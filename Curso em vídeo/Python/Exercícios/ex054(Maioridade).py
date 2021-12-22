from datetime import date
ano = date.today().year
s = 0
for c in range(0, 7):
    idade = int(input('Digite seu ano de nascimento: '))
    if ano - idade >= 21:
        idade = 1
        s = s + idade
print('Das 7 pessoas, {} são maiores de idade e {} ainda não atingiram a maioridade.'.format(s, 7 - s))
