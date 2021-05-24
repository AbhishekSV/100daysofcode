from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    
    def create_car(self):
        dice = randint(1,6)
        if dice == 1:
            pos = (300, randint(-250,250))
            car = Turtle()
            car.shape("square")
            car.color(choice(COLORS))
            car.penup()
            car.goto(pos)
            car.setheading(180)
            car.resizemode("user")
            car.shapesize(stretch_wid = 1, stretch_len = 2)
            self.cars.append(car)
    
    
    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)
    
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT