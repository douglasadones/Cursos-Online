from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-200, 250)
        self.update_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.hideturtle()
        self.level = 1
        self.home()
        self.penup()
        self.write(arg="GAME OVER", align="center", font=FONT)



