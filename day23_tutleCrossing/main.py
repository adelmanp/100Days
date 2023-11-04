#!/usr/bin/python3

import time
import logging
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    car_manager.new_car()

    # Detect Collision
    cars = car_manager.cars
    for car in cars:
        if car.distance(player) < 20:
            logging.debug("Collision detected")
            game_is_on = False
            scoreboard.game_over()

    # Detect if level completed
    if player.is_at_finish_line():
        logging.debug("Level complete")
        scoreboard.new_level()
        player.turtle_reset()
        car_manager.speed_increase()

screen.exitonclick()
