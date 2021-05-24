from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def re_appear(self):
        self.goto(STARTING_POSITION)
    
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.re_appear()
    
    
    def jump(self):
        self.forward(MOVE_DISTANCE)
    
    
    def reached_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
