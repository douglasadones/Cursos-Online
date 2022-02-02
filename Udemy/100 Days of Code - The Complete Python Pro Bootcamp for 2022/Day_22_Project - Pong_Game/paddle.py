from turtle import Turtle
STEPS = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up1(self):
        new_y = self.ycor() + STEPS
        self.goto(self.xcor(), new_y)

    def go_down1(self):
        new_y = self.ycor() - STEPS
        self.goto(self.xcor(), new_y)

    def go_up2(self):
        new_y = self.ycor() + STEPS
        self.goto(self.xcor(), new_y)

    def go_down2(self):
        new_y = self.ycor() - STEPS
        self.goto(self.xcor(), new_y)
