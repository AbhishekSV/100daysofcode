from turtle import Turtle
from os import path, sys

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align = ALIGNMENT, font = FONT)
    
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 270)
        self.score = 0
        with open(path.join(sys.path[0],"snake_module/highscore.txt"),"r") as f:
            self.highscore = int(f.read())
        self.print_score()
    
    
    def add_score(self):
        self.score += 1
        self.print_score()
    
    
    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(path.join(sys.path[0],"snake_module/highscore.txt"),"w") as fl:
                fl.write(f"{self.highscore}")
        self.score = 0
        self.print_score()
    
    
    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.write("GAME OVER!", False, align = ALIGNMENT, font = FONT)