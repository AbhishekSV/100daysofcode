from turtle import Screen
from snake_module.snake import Snake
from snake_module.food import Food
from snake_module.scoreboard import Scoreboard
import time

canvas = Screen()
canvas.setup(width = 600, height = 600)
canvas.bgcolor("black")
canvas.title("Classic Snake Game")
canvas.tracer(0)

python = Snake()
rat = Food()
score = Scoreboard()

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
    h = python.head
    
    #Detect collision with body
    for segment in python.snake_body[1:]:
        if h.distance(segment) < 10:
            score.game_over()
            game_on = False
    
    #Detect collision with Wall
    if h.xcor() > 280 or h.xcor() < -280 or h.ycor() > 280 or h.ycor() < -280:
        score.game_over()
        game_on = False
    
    #Detect collision with Food
    if h.distance(rat) < 15:
        rat.refresh()
        python.add_body()
        score.add_score()

canvas.exitonclick()