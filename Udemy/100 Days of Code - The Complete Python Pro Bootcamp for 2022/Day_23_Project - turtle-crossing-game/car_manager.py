from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        random_chance = randint(1, 6)  # less cars generated :D
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(300, randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for move in range(0, len(self.all_cars)):
            self.all_cars[move].backward(self.car_speed)

    def more_car_speed(self):
        self.car_speed += MOVE_INCREMENT
