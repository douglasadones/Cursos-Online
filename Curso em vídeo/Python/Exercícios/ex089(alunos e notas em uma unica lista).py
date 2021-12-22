#Progama que leia nome e duas notas de vários alunos e guarde tudo em lista composta.
#No final, mostre um boletim ontendo a média de cada um e permita que o usuário possa mostrar as notas
#de cada aluno individualmente.
cadastros = list()
nomes = list()
notas = list()
while True:
    nomes.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nomes.append(notas[:])
    cadastros.append(nomes[:])
    nomes.clear()
    notas.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*20)
print('No. NOME {:>16}'.format("MÉDIA"))
print('-'*30)
for c in range(0, len(cadastros)):
    print(f'{c:<3} {cadastros[c][0]:<15}{(cadastros[c][1][0] + cadastros[c][1][1]) / 2:>7}')
print('-'*40)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    print(f'Notas de {cadastros[n][0]} são {cadastros[n][1]}')
    print('-' * 40)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
