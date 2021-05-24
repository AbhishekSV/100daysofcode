from turtle import Turtle

class Scoreboard(Turtle):
    
    def print_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_1, align = "center", font = ("Courier-Bold", 80,"normal"))
        self.goto(100, 200)
        self.write(self.score_2, align = "center", font = ("Courier-Bold", 80,"normal"))
    
    
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.print_score()
    
    
    def point_1(self):
        self.score_1 += 1
        self.print_score()
        
    
    def point_2(self):
        self.score_2 += 1
        self.print_score()