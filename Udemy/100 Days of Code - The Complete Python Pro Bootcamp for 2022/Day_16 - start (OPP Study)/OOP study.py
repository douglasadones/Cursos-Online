# Estudando OOP e estudando a aplicação de atributos e métodos
# atributos são variáveis e métodos são funções.


# import another_module
# print(another_module.another_variable)
# Link da documentação da biblioteca turtle: https://docs.python.org/3/library/turtle.html
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")  # Muda a forma do Dimmy na tela
# timmy.color("BlueViolet")  # Muda a cor (link: https://cs111.wellesley.edu/labs/lab01/colors)
# timmy.forward(100)  # Timmy moverá 100 vezes para frente
#
# my_screen = Screen()  # Mostra a tela
# print(my_screen.canvheight)  # Mostra o tamanho da tela no console
# my_screen.exitonclick()  # Mantém a tela até que cliquemos nela.

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
table.align = "l"  # mudando um atributo de um objeto
table.valing = "b"

print(table)
