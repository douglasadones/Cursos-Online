#programa que leia o nome completo e mostre tudo em maiúsculo, minúsculo, quantas letras(sem os espaços)
# e quantas letras tem o primeiro nome.
nome = str((input('Digite o seu nome Completo: '))).strip() #botei str() e já eliminei os espaços inúteis com .strip().
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print(len(nome)) #quantidade de caracteres (com espaços)
space = nome.replace(' ', '') #retirei os espaços
print('Seu nome possui {} caracteres.'.format(len(space))) #quantidade de caracteres sem o espaço
lista = nome.split() #transformei em uma lista
primeiro = lista[0]
print('Seu primeiro nome é {} e ele tem {} caracteres.'.format(lista[0], len(primeiro))) #palavra 0 da lista 'primeiro'
# print('Seu primeiro nome é {} e ele tem {} caracteres.'.format(lista [0], nome.find(' '))) aqui eu pedi para ele procurar o primeiro espaço;.
