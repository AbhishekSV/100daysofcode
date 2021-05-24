import time
from turtle import Screen
from crossing_module.player import Player
from crossing_module.car_manager import CarManager
from crossing_module.scoreboard import Scoreboard

canvas = Screen()
canvas.setup(width=600, height=600)
canvas.tracer(0)

user = Player()
score = Scoreboard()
car_manager = CarManager()

canvas.listen()
canvas.onkey(user.jump, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    canvas.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    #Detect collision with car
    for car in car_manager.cars:
        if car.distance(user) < 20:
            game_is_on = False
            score.game_over()
    
    #Detect successful crossing
    if user.reached_finish_line():
        score.levelup()
        user.re_appear()
        car_manager.level_up()

canvas.exitonclick()