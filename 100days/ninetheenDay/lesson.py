from turtle import Turtle, Screen

timmy = Turtle()


def move_forward():
    timmy.fd(10)


def move_backward():
    timmy.backward(10)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


def move_clockwise():
    timmy.right(10)


def move_counter_clockwise():
    timmy.left(10)


screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()