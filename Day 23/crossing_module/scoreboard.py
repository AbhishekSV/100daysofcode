from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    
    def levelup(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, align = ALIGNMENT, font = FONT)
    
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("black")
        self.goto(-240,260)
        self.levelup()
    
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align = ALIGNMENT, font = FONT)
