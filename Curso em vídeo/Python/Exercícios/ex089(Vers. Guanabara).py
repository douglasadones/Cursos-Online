#Progama que leia nome e duas notas de vários alunos e guarde tudo em lista composta.
#No final, mostre um boletim ontendo a média de cada um e permita que o usuário possa mostrar as notas
#de cada aluno individualmente.
nome = list()
nota1 = list()
nota2 = list()
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media]) #isso aqui é muito interessante e importante!
    r = ' '
    while r not in 'SN':
        r = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    print(f'Notas de {ficha[n][0]} são {ficha[n][1]}')
    print('-' * 40)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
