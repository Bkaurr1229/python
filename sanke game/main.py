import time
from food import Food
from turtle import Screen, Turtle
from snake import Snake
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()  # initialize the snake using snake class
food = Food()  # initialize the food using food class
score = Scoreboard()

screen.listen()
# for keyboard access
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_on = False
        score.reset()
        snake.reset()
        # score.Game_over()

    # detect collision with tail
    for segments in snake.segment[5:1]:
        if snake.head.distance(segments) < 10:
            game_on = False
            score.reset()
            snake.reset()
            # score.Game_over()

screen.exitonclick()
