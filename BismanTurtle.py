from turtle import Turtle, Screen
import random
colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan",
    "magenta", "brown", "black", "gray", "lime", "violet", "indigo",
    "turquoise", "gold", "silver", "coral", "navy"
]
timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def move_anticlockwise():
   timmy.left(10)

def move_clockwise():
   timmy.right(10)

def move_clear():
    timmy.clear()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_anticlockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=move_clear)

screen.exitonclick()