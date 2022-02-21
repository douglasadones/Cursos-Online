# # Printando os dados do arquivo weather_data.csv
# with open("weather_data.csv") as data_file:
#     data = file.readlines()
#     print(data)


# # Usando a biblioteca csv para criar uma lista contendo as temperaturas do arquivo weather_data já no tipo int.
# import csv
# data = []
# with open("weather_data.csv") as data_file:
#     file = csv.reader(data_file)
#     temperatures = []
#     for row in file:
#         if not row[1] == "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)  # tabela com todas as informações
# print(data["day"])  # Apenas os dias
# # ou print(data.day)
# print(data["temp"])  # Apenas as temperaturas
# # ou print(data.temp)
# print(data["condition"])  # apenas as condições
# # ou print(data.condition)
#
# data_dict = data.to_dict()  # Converte para um diconário
# print(data_dict)
#
# temp_list = data["temp"].to_list()  # converte uma série para uma lista
# print(temp_list)
#
# # Calculando a temperatura média.
# # Primeiro método (sem usar a biblioteca pandas:
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
#
# # Segundo método (Usando a biblioteca pandas)
# print(data["temp"].mean())
#
# # Obtendo o valor máximo de uma série
# print(data["temp"].max())


# # Obtendo uma linha de uma tabela
# print(data[data.temp == data.temp.max()])  # Quando usamos condições, o retorno é uma linha


# # Conseguindo dados de um dia específico:
# monday = data[data.day == "Monday"]
# print(monday.condition)  # Aqui será mostrado apenas a condição da segunda-feira.
#
# # Obtendo a temperatura da segunda-feira e convertendo para Fahrenheit
# monday_tempo_F = (monday.temp * 9/5) + 32
# print(monday_tempo_F)


# # Criando uma moldura / tabela de dados do zero:
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
# new_data = pandas.DataFrame(data_dict)  # Essa classe faz o serviço completo, basta por os dados como parâmetro.
# print(new_data)
# new_data.to_csv("new_data.csv")  # Transformando os dados em um arquivo .csv


import pandas

squirrel = pandas.read_csv("Squirrel_Data.csv")

grey_squirrels_count = len(squirrel[squirrel["Primary Fur Color"] == "Gray"])  # O len() vai contar quantas linhas.
red_squirrels_count = len(squirrel[squirrel["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel[squirrel["Primary Fur Color"] == "Black"])

new_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

data = pandas.DataFrame(new_dict)  # Construindo a tabela
data.to_csv("Squirrel_count.csv")  # transformando em um arquivo .csv
print(data)

