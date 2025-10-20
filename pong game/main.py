from paddle import Paddle
from turtle import Screen, Turtle
from paddle import Ball , Scoreboard
from random import random
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = Scoreboard()


# for i in range(100):
#     steps = int(towards(350,0) )
#     angle = int(towards() )
#     ball.right(angle)
#     ball.fd(steps)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "r")
screen.onkey(l_paddle.go_down, "f")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # detection with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    # detection with paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:

        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.reset_position()
        score_board.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

    ball.move()

# paddle1 = Paddle()
#
# paddle1.Create_paddle()


screen.exitonclick()
