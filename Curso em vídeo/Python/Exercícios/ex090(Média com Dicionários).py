#Programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo
# da estrutura na tela.
dados = {}
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
print('-=' * 30)
if dados['média'] >= 7:
    dados['situação'] = 'Aprovado(a)'
elif 5 <= dados['média'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado(a)'
for k, v in dados.items():
    print(f'    - {k} é igual a {v}')
