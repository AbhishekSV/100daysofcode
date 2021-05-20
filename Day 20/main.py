from turtle import Turtle, Screen
from snake_module.snake import Snake
import time

canvas = Screen()
canvas.setup(width = 600, height = 600)
canvas.bgcolor("black")
canvas.title("Classic Snake Game")
canvas.tracer(0)

python = Snake()

canvas.listen()
canvas.onkey(python.up, "Up")
canvas.onkey(python.down, "Down")
canvas.onkey(python.left, "Left")
canvas.onkey(python.right, "Right")

game_on = True
while game_on:
    canvas.update()
    time.sleep(0.1)
    
    python.move()

canvas.exitonclick()