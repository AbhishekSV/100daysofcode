from turtle import Turtle
import random

class Food(Turtle):
    
    def refresh(self):
        self.goto(random.randint(-280,280), random.randint(-280,280))
    
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed(0)
        self.refresh()