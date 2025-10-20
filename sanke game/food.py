from turtle import Turtle
import random


class Food(Turtle):
    # created food

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
