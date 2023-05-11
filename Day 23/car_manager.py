import random

from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(310, random.randint(-250, 250))

    def move(self, speed):
        new_x = self.xcor() - speed
        self.goto(new_x, self.ycor())


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def generate_car(self):
        for x in range(random.randint(1, 10)):
            if x == 7:
                car = Car()
                self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move(self.speed)
            if car.xcor() < -310:
                self.cars.remove(car)

    def check_distance(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False

    def refresh_cars(self):
        self.cars = []

    def level_up(self):
        self.speed *= MOVE_INCREMENT
