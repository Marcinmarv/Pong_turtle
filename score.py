from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_left} = {self.score_right}", align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.score_left += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_right(self):
        self.score_right += 1
        self.clear()
        self.update_scoreboard()