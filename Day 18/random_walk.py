import random
from turtle import Turtle, Screen, colormode

tim = Turtle()
tim.shape("turtle")
colormode(255)

colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'SeaGreen']
tim.pensize(10)
tim.speed(10)
comands = [0, 90, 180, 270]


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


for _ in range(50):
    tim.color(random_color())
    tim.setheading(random.choice(comands))
    tim.forward(30)

screen = Screen()
screen.exitonclick()
