#Progama que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso
#a CTPS for diferente de ZERO, o dicionário receberá também p ano de contratação e o salário. Calcule e acrescente, além
#da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
cadastro['idade'] = date.today().year - nascimento
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$: '))
    cadastro['aposentadoria'] = (cadastro['contratação'] - nascimento) + 35
print('-=' * 20)
for k, v in cadastro.items():
    print(f'    - {k} tem o valor {v}')
