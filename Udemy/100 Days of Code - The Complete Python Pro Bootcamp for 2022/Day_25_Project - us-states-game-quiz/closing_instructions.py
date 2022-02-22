from turtle import Turtle

GUIDE = "Type 'exit' to end the Quiz and create a .csv file with the missing states"
FONT = "Arial"
FONT_SIZE = 15


class Instructions(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(-1, 250)
        self.write(arg=GUIDE, align="Center", font=(FONT, FONT_SIZE, "normal"))
        self.goto(0, -275)
        self.write(arg="Good Lucky!", align="Center", font=(FONT, FONT_SIZE, "normal"))
