from turtle import Turtle, Screen
# import turtle as t

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSeaGreen4")


def draw_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)


def draw_dotted_line():
    for _ in range(10):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


draw_dotted_line()
screen = Screen()
screen.exitonclick()