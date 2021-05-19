from turtle import Turtle, Screen, clearscreen
from random import randint,choice

# # Creates Etch-A-Sketch App
# def move_forward():
#     tony.forward(100)

# def move_backward():
#     tony.backward(100)

# def move_anti_clockwise():
#     tony.left(tony.heading() + 10)

# def move_clockwise():
#     tony.right(tony.heading() + 10)

# def clean():
#     tony.clear()
#     tony.penup()
#     tony.home()
#     tony.pendown()

# canvas.listen()
# canvas.onkey(key = "w", fun = move_forward)
# canvas.onkey(key = "s", fun = move_backward)
# canvas.onkey(key = "a", fun = move_anti_clockwise)
# canvas.onkey(key = "d", fun = move_clockwise)
# canvas.onkey(key = "c", fun = clean)

# Creates Turtle Race Bet App
game_on = False
canvas = Screen()
canvas.setup(width=500, height=400)
user_bet = canvas.textinput(title = "Make a bet", prompt = "Which color turtle will win the race? Enter a color from VIBGYOR: ")
colors = ["red", "green", "orange", "yellow", "blue", "purple"]
turtles = []

for i in range(0,6):
    tony = Turtle(shape="turtle")
    tony.color(colors[i])
    tony.penup()
    tony.goto(x=-230, y=-100+(i*40))
    turtles.append(tony)

if user_bet:
    game_on = True

while game_on:
    for t in turtles:
        if t.xcor() > 230:
            game_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've Won!. The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost!. The {winning_color} turtle is the winner!")                
        t.forward(randint(0,10))

canvas.exitonclick()