import turtle as t
from random import choice

# # Extraindo Cores de uma imagem
# import colorgram as c
# rgb_color = []
# rgb_tuple = ()
# colors = c.extract("hirst-painting.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_color.append(rgb_tuple)
#
# print(rgb_color)

color_list = [(238, 250, 244), (187, 18, 44), (243, 231, 66), (252, 235, 239), (210, 236, 242), (196, 75, 32),
              (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214),
              (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50),
              (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55),
              (4, 86, 111), (162, 29, 27), (234, 171, 164), (162, 212, 176)]

# Pintando um quadro com pontos 10 x 10
t.colormode(255)
be = t.Turtle()
be.hideturtle()
be.speed(0)
y = -220
for position in range(10):
    be.penup()
    be.goto(-235, y)
    for move in range(10):
        be.dot(20, choice(color_list))
        be.forward(50)
    y += 50

scream = t.Screen()
scream.exitonclick()

