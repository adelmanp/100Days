

import random
import logging
from turtle import Turtle

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.new_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_cars(self):
        logging.debug(f"Car speed: {self.car_speed}")
        for car in self.cars:
            car.backward(self.car_speed)

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT
