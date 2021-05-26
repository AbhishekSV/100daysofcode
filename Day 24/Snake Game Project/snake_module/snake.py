from turtle import Turtle
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def add_body(self):
        body = Turtle()
        body.shape("square")
        body.color("white")
        body.penup()
        body.setpos(self.snake_body[-1].xcor()-20,self.snake_body[-1].ycor())
        self.snake_body.append(body)
    
    
    def __init__(self):
        self.snake_body = []
        head = Turtle()
        head.shape("square")
        head.color("white")
        head.penup()
        self.snake_body.append(head)
        for i in range(2):
            self.add_body()
        self.head = self.snake_body[0]
    
    
    def reset_snake_body(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        head_r = Turtle()
        head_r.shape("square")
        head_r.color("white")
        head_r.penup()
        self.snake_body.append(head_r)
        for i in range(2):
            self.add_body()
        self.head = self.snake_body[0]
    
    
    def move(self):
        for segment in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[segment].setpos(self.snake_body[segment-1].position())
        self.head.forward(DISTANCE)
    
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
