from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("data.txt") as data:
           self.high_score = int (data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE :{self.score}", align="center", font=('Arial', 8, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def Game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over", align="center", font=('Arial', 8, 'normal'))
    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"SCORE :{self.score}", align="center", font=('Arial', 8, 'normal'))