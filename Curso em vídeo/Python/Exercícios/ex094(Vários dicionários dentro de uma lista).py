# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas, B) A média de idade do grupo
# C) uma lista com todos as mulheres e C) Uma lista com todas as pessoas com idade acima da média.
dados = dict()
cadastros = list()
totidade = 0
while True:
    r = ' '
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = ' '
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while dados['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    dados['idade'] = int(input('Idade: '))
    cadastros.append(dados.copy())
    totidade += dados['idade']
    r = str(input('Quer continuar?: [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        r = str(input('Quer continuar?: [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
med = totidade / len(cadastros)
print('-=' * 25)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas.')
print(f'B) A média de idade é de {med:.2f} anos')
print('C) As mulheres cadastradas foram:', end=' ')
for c in cadastros:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print()
print('D) Lista das pessoas que estão acima do média:')
for c in cadastros:
    if c['idade'] > med:
        for k, v in c.items():
            print(f'    {k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
