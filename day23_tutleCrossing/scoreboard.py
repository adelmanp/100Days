from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.goto(-250, 270)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 14, "normal"))

    def new_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 20, "bold"))
