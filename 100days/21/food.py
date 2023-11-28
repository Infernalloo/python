from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

    def move(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(x=random_x, y=random_y)
