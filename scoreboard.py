FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level=1
        self.penup()
        self.goto(-280,260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f'LEVEL: {self.level}', align='left', font=FONT)

    def increase_level(self):
        self.level+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over at LEVEL: {self.level}', align='center', font=FONT)