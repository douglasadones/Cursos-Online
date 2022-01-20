# Estudando a biblioteca turtle para entender a aplicação de OOP e consulta da documentação de um módulo.

from turtle import Turtle, Screen
from random import randint, choice
from time import sleep


tim = Turtle()
tim.shape("turtle")
tim.color("MediumAquamarine")
Screen().colormode(255)

# # Drawing a square
# for side_square in range(4):
#     tim.forward(100)
#     tim.right(90)

# # Drawing a dashed line
# for steps in range(5):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# # Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon.
# # Drawing a triangle
# side = 3
# while side < 11:
#     for _ in range(side):
#         tim.forward(100)
#         tim.right(360 / side)
#     tim.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
#     side += 1
#
#
# # Angela Version
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)


# # Draw a Random walk
# directions = [0, 90, 180, 270]
# tim.speed(0)
# tim.pensize(10)
# for move in range(200):
#     tim.setheading(choice(directions))
#     tim.forward(randint(20, 40))
#     tim.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))

# Draw a spirograph
tim.speed(0)
direction = 5
for _ in range(72):
    tim.circle(100)
    tim.setheading(direction)
    tim.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    direction += 5

screen = Screen()
screen.exitonclick()
