from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up1, "Up")
screen.onkey(r_paddle.go_down1, "Down")
screen.onkey(l_paddle.go_up2, "w")
screen.onkey(l_paddle.go_down2, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    sleep(ball.move_speed)

    # Detectando colisão com as paredes
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # Detectando colisão com as raquetes
    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bouce_x()

    # Detectando a raquete direita erra a bola
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Detectando a raquete esquerda erra a bola
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
