# try:
#     file = open("a_file.txt")  # Documento inexistente
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:  # Caso não exista erros
#     content = file.read()
#     print(content)
# finally:  # finally acontece independente se ouve houver ou não erros.
#     raise TypeError("this is an error that I made up.")  # Você pode "gerar" uma mensagem de erro.


# Exemplo de uso do raise
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human should not be over 3 meters.")
