# Programa que leia o sexo de uma pessoa mas só aceite M ou F
'''sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o sexo da pessoa [M/F]: '))'''

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Por favor, informe  seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
