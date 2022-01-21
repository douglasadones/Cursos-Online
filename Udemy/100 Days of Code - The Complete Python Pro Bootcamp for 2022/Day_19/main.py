# Estudo de Função de Ordem Superior
from turtle import Turtle, Screen

be = Turtle()
screen = Screen()


def move_forwards():
    be.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
