from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_color_choice = screen.textinput(title="Put you bet", prompt="Color of the turtle: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cord = [-150, -110, -70, -30, 10, 50]

for turtle_index in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[turtle_index])
    timmy.goto(x=-235, y=y_cord[turtle_index])

screen.exitonclick()
