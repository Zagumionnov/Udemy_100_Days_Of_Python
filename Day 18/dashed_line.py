from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

for n in range(20):
    if n % 2 == 0:
        tim.pendown()
        tim.forward(10)
    tim.penup()
    tim.forward(10)


screen = Screen()
screen.exitonclick()
