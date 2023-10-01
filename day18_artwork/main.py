#!/usr/bin/python3

import random
from turtle import Turtle, Screen


colors = [
          (202, 164, 110), (236, 239, 243), (149, 75, 50), (168, 99, 102), (176, 192, 208),
          (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), 
          (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), 
          (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), 
          (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), 
          (12, 70, 64), (107, 127, 153)
          ]

# setup the object and screen
pen = Turtle()
pen.hideturtle()
screen = Screen()
screen.colormode(255)
pen.speed("fastest")


# Select a color
def select_color():
    return random.choice(colors)


# draw a row of dots 
def draw_row():
    for column in range(10):
        dot_color = select_color()
        pen.dot(20, dot_color)
        pen.up()
        pen.forward(50)
        pen.down()
   
# reset to start a new line
def new_line_start():
    pen.up()
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(500)
    pen.right(180)
    pen.down()


# set pen to starting point
pen.penup()
pen.setx(-200)
pen.sety(-200)
pen.position()
pen.down()


for row in range(10):
    draw_row()
    new_line_start()


screen.exitonclick()