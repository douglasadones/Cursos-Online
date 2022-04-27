import json

site = input("Site: ")
email = input("email: ")
password = input("Password: ")

# try:
#     file = open("data.json", "r")
#     file.read()
#     file.close()
# except FileNotFoundError:
#     file = open("data.json", "w")
#     file.close()

new_data = {site: {
    "email": email,
    "password": password,
    }
}


# Preenchendo um novo .json.
with open("data.json", "w") as file:
    json.dump(new_data, file, indent=4)  # indent=4 diz as quebras de linha para facilitar a leitura.

# Lendo um arquivo .json
with open("data.json", "r") as file:
    data = json.load(file)  # Já transforma um .json em um dicionário do python.
    print(data)



# Adicionando dados em um .json existente
with open("data.json", "r") as file:
    # Reading old data
    data = json.load(file)
    # Updating old data with new data
    data.update(new_data)

with open("data.json", "w") as file:
    # Saving updated data
    json.dump(data, file, indent=4)  # cuidado com os parâmetros usados.
