from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align = ALIGNMENT, font = FONT)
    
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 270)
        self.score = 0
        self.print_score()
    
    
    def add_score(self):
        self.score += 1
        self.print_score()
    
    
    def game_over(self):        
        self.setpos(0, 0)
        self.write("GAME OVER!", False, align = ALIGNMENT, font = FONT)