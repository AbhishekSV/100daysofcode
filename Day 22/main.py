from turtle import Screen
from pong_module.paddle import Paddle
from pong_module.ball import Ball
from pong_module.scoreboard import Scoreboard
import time

canvas = Screen()
canvas.bgcolor("black")
canvas.setup(width = 800, height = 600)
canvas.title("Pong")
canvas.tracer(0)

paddle_1 = Paddle((-350,0))
paddle_2 = Paddle((350,0))
pong_ball = Ball()
score = Scoreboard()

canvas.listen()
canvas.onkey(paddle_1.up, "w")
canvas.onkey(paddle_1.down, "s")
canvas.onkey(paddle_2.up, "Up")
canvas.onkey(paddle_2.down, "Down")

game_on = True
while game_on:
    time.sleep(pong_ball.move_speed)
    canvas.update()
    pong_ball.move()
    
    #Detect collision with Wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()
    
    #Detect collision with Paddles
    if (pong_ball.distance(paddle_2) < 50 and pong_ball.xcor() > 320) or (pong_ball.distance(paddle_1) < 50 and pong_ball.xcor() > -320):
        pong_ball.bounce_x()
    
    #Detect left paddle miss
    if pong_ball.xcor() < -380:
        pong_ball.miss()
        score.point_2()
    
    
    #Detect right paddle miss
    if pong_ball.xcor() > 380:
        pong_ball.miss()
        score.point_1()

'''
margin = Turtle()
margin.hideturtle()
margin.penup()
margin.pencolor("white")
margin.goto(0,300)
margin.setheading(270)
margin.speed(0)
for i in range(0,300,20):
    margin.pendown()
    margin.forward(20)
    margin.penup()
    margin.forward(20)
'''

canvas.exitonclick()