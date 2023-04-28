import random
from turtle import Turtle, Screen, colormode

tim = Turtle()
colormode(255)
tim.speed(10)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


for _ in range(36):
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)

screen = Screen()
screen.exitonclick()
