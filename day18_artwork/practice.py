#!/usr/bin/python3
# this is a file for learning how to work with turtle and practice calling and using the turtle object.

from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.pensize(2)
timmy.speed("fastest")


# draw a square 
# for side in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# draw a dashed line
# for line in range(10):
#     timmy.forward(10)
#     timmy.pu()
#     timmy.forward(10)
#     timmy.pd()

# set random color on turtle
def change_color(turtle_name):
    R = random.random()
    B = random.random()
    G = random.random()


    turtle_name.color(R, G, B)

# draw geometric shapes
# def shape_drawer(sides, turtle_name):
#     change_color(turtle_name)
#     angle = 360 / sides
#     for side in range(sides):
#         turtle_name.forward(150)
#         turtle_name.left(angle)

# for sides in range(3, 11):
#     shape_drawer(sides, timmy)


# random walk
# def walk_drawer(steps, turtle_name):
#     directions = [0, 90, 180, 270]
#     for step in range(steps):
#         change_color(turtle_name)
#         heading = random.choice(directions)
#         turtle_name.setheading(heading)
#         turtle_name.forward(75)

# walk_drawer(200, timmy)

# circle drawer
def circle_drawer(turtle_name, degrees):
    heading = 0
    for circle in range(int(360 / degrees)):
        change_color(turtle_name)
        turtle_name.setheading(heading)
        turtle_name.circle(100)
        heading += degrees

circle_drawer(timmy, 5)


screen.exitonclick()