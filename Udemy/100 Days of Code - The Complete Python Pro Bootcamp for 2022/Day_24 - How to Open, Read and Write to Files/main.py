file = open("my_file.txt")  # Abre o arquivo
contents = file.read()  # Armazena o conteúdo na variável "contents"
print(contents)
file.close()  # Fecha o arquivo (Evitando uso desnecessário de processamento)

# Para não ter a necessidade de fechar o arquivo (e a possibilidade de esquecer de fazê-lo) podemos usar o
# comando "with" que irá realizar o trabalho e fechar logo em seguida:

with open("my_file.txt", mode="r") as file:  # "as" (nome da variável)
    contents = file.read()
    print(contents)

# Se quisermos escrever algo no documento substituindo as informações nele contidas, precisamos mudar o modo do
# arquivo, "w" no caso. Isso irá substituir as informações pela informação que você quiser:

with open("my_file.txt", mode="w") as file:  # "as" (nome da variável)
    file.write("New text.")  # Substitui o conteúdo existente pelo informado. ("new text") no caso.

# Caso não queira substituir e sim adicionar novas informações, use o modo "a" (append):

with open("my_file.txt", mode="a") as file:  # "as" (nome da variável)
    file.write("\nNew text again :D.")  # Adiciona alguma informação. ("new text") no caso.

# Caso use o modo "w" e informe um documento que não exista, o documento será criado. Veja:

with open("new_file.txt", mode="w") as file:
    file.write("New text.")

# Abrindo um arquivo que está em outra pasta do computador (Usando a posição Absoluta do arquivo):

file = open("/Users/adone/Downloads/Estudos_Programação/other_file.txt")  # Abre o arquivo
contents = file.read()  # Armazena o conteúdo na variável "contents"
print(contents)
file.close()


# Abrindo um arquivo que está em outra pasta do computador(Usando a posição relativa do arquivo):

file = open("../../../Downloads/Estudos_Programação/outro_test.txt")  # Abre o arquivo
contents = file.read()  # Armazena o conteúdo na variável "contents"
print(contents)
file.close()
