from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(pos)
        self.resizemode("user")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
    
    
    def up(self):
        if self.ycor() <= 230:
            self.setpos(self.xcor(), self.ycor()+20)
    
    
    def down(self):
        if self.ycor() >= -220:
            self.setpos(self.xcor(), self.ycor()-20)