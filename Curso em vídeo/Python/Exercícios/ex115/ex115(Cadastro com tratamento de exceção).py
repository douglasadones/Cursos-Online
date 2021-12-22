# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from ex115.defs.interface import * # (*) diz pra inportar tudo
from ex115.defs.arquivo import *
from time import sleep

arq = 'cursoemVideo.txt'

# Verificação e criação de arquivo
if arquivoExiste(arq): #Função lá no pacote arquivo
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq) #Função lá no pacote arquivo

'''
Ou posso fazer nessa sintaxe menos explicativa:
if not arquivoExiste(arq)
    criarArquivo(arq)
'''

# Menu
while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1: #Opção de listagem de conteúdo de um arquivo
        lerArquivo(arq)
        sleep(2)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(2)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
        sleep(2)
