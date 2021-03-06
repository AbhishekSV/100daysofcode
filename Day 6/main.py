def move():
    print("Bot goes straight")

def turn_left():
    print("Bot turns left")

def right_is_clear():
    print("Bot checks right")

def front_is_clear():
    print("Bot checks straight")

def wall_in_front():
    print("Bot checks straight wall")

def wall_on_right():
    print("Bot checks right wall")

def at_goal():
    print("Bot is at goal")

#Day 6 Assignment 1,2
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()

#Day 6 Assignment 1,2,3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()

#Day 6 Assignment 1,2,3,4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()

#Day 6 App
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()