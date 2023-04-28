from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

for turns in range(3, 9):
    for _ in range(turns):
        angle = 360 / turns
        tim.forward(100)
        tim.left(angle)


screen = Screen()
screen.exitonclick()
