from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Desativa as animações

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()   # inicia o método para reconhecimento de teclas
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake. right, "Right")


game_is_on = True
while game_is_on:
    screen.update()  # ativa as animações
    sleep(0.1)
    snake.move()

    # Detectando colisão com a comida
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detectando colisão com a parede
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detectando colisão com a cauda
    for segment in snake.segments[1:]:  # o [1:] exclui a cabeça da cobra.
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
