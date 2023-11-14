from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("PySnake by Inferno")
starting_xcor = [0, -20, -40]

for snake_body in range(3):
    tim = Turtle(shape="square")
    tim.color("white")
    tim.penup()
    tim.goto(x=starting_xcor[snake_body], y=0)

screen.exitonclick()
