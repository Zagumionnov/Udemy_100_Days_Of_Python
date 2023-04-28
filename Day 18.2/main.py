import random

import colorgram
from turtle import Turtle, Screen, colormode

tim = Turtle()
colormode(255)

colors = colorgram.extract('image.jpg', 9)
rgb_colors = [color.rgb for color in colors]
step_length = 20
square_width = 6


def to_next_line():
    tim.left(90)
    tim.forward(step_length)
    tim.right(90)
    tim.backward(step_length * square_width)


for line in range(square_width):
    for _ in range(square_width):
        tim.color(random.choice(rgb_colors))
        tim.penup()
        tim.forward(step_length)
        tim.dot(10)
    if line + 1 != square_width:
        to_next_line()


screen = Screen()
screen.exitonclick()
