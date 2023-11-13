from turtle import Turtle, Screen
import random

race_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_color_choice = screen.textinput(title="Put you bet", prompt="Color of the turtle: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cord = [-150, -110, -70, -30, 10, 50]
all_turtles = []

for turtle_index in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[turtle_index])
    timmy.goto(x=-235, y=y_cord[turtle_index])
    all_turtles.append(timmy)


while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_color_choice:
                print(f"You've won, The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost, The {winning_color} turtle is the winner.")
        random_fd = random.randint(0, 10)
        turtle.forward(random_fd)

screen.exitonclick()
