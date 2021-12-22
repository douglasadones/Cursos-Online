# Estrutura condicional Aninhada (Em formato de ninho, uma coisa dentro da outra)
nome = str(input('Qual é o seu nome? '))
if nome == 'Douglas':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Alice Jéssica Brenda':
    print('Belo nome feminino')
else:                                   # o else é opcional
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
