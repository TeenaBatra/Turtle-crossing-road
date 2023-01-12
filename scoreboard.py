FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.display_level()

    def display_level(self):
        self.goto(-280, 270)
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
