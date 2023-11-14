from turtle import Turtle, Screen
import time

game_over = False
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("PySnake by Inferno")
screen.tracer(0)

starting_xcor = [0, -20, -40]
body_squares = []

for snake_body in range(3):
    tim = Turtle(shape="square")
    tim.color("white")
    tim.penup()
    tim.goto(x=starting_xcor[snake_body], y=0)
    body_squares.append(tim)

while not game_over:
    screen.update()
    time.sleep(0.1)

    for body_num in range(len(body_squares) - 1, 0, -1):
        new_x = body_squares[body_num - 1].xcor()
        new_y = body_squares[body_num - 1].ycor()
        body_squares[body_num].goto(x=new_x, y=new_y)
    body_squares[0].fd(20)
    body_squares[0].left(90)

screen.exitonclick()
