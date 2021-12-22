#Programa que leia o nome de uma cidade e diga se ela começa com o nome 'SANTO' ou não.
cidade = str(input('Escreva o nome de uma cidade qualquer: ')).strip().capitalize() #garanti a exclusão dos espaços e a formatação do nome "Santo"
print('O nome da cidade começa com "Santo"? {}'.format('Santo' in cidade)) #poderia ser: .format(cidade[:5] == 'Santo')

#Programa que leia o nome de uma pessoa e verifique se tem "Silva" no seu nome.
nome = str(input('Escreva seu nome completo: ')).strip().title()
print('Seu nome possui "Silva"? {}'.format('Silva' in nome))
