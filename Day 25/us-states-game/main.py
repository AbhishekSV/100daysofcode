import turtle
from os import path, sys
import pandas

canvas = turtle.Screen()
canvas.title("U.S. States Game")
image = "/Users/abhisheksabnivis/Desktop/100daysofcode/Day 25/us-states-game/Data/blank_states_img.gif"
canvas.addshape(image)
turtle.shape(image)
score = 0
df = pandas.read_csv(path.join(sys.path[0],"Data/50_states.csv"))
all_states = df.state.to_list()
guessed_states = []
# user_state = df[df.state.str.lower() == 'delaware']
# s = user_state.state
# print(s.values[0])

while len(guessed_states) < 51:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.pencolor("black")
    user_answer = canvas.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if user_answer == "Exit":
        # states to learn.csv
        states_remaining = []
        for us_state in all_states:
            if us_state not in guessed_states:
                states_remaining.append(us_state)
        missing_states = pandas.DataFrame(states_remaining)
        missing_states.to_csv("states_to_learn.csv")
        break
    if user_answer in all_states:
        user_state = df[df.state == user_answer]
        t.setpos(int(user_state.x),int(user_state.y))
        t.write(f"{user_state.state.item()}",False, align = "center", font = ("Arial", 8, "normal"))
        guessed_states.append(user_answer)

