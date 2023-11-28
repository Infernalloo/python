from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars_list = []

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.penup()
            car.setheading(0)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(x=300, y=random.randint(-250, 250))
            self.cars_list.append(car)

    def move_cars(self):
        for car in self.cars_list:
            car.backward(STARTING_MOVE_DISTANCE)
