from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

y = -100
for turtle in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle)
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y)
    all_turtle.append(new_turtle)
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! the {winning_color} turtle is te winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is te winner!")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()
