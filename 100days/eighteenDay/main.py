from turtle import Turtle, Screen
import random
# import turtle as t

timmy = Turtle()
timmy.shape("turtle")
colors = ["OliveDrab", "Olive", "RoyalBlue", "Chocolate", "Indigo", "PaleVioletRed", "SlateGray", "DarkSeaGreen4"]
angles = [0, 90, 180, 270]
timmy.speed("fast")


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


def draw_pentagon():
    for _ in range(5):
        timmy.forward(100)
        timmy.left(72)


def draw_hexagon():
    for _ in range(6):
        timmy.forward(100)
        timmy.left(60)


def draw_heptagon():
    for _ in range(7):
        timmy.forward(100)
        timmy.left(51)


def draw_octagon():
    for _ in range(8):
        timmy.fd(100)
        timmy.left(45)


def draw_nonagon():
    for _ in range(9):
        timmy.fd(100)
        timmy.left(40)


def draw_decagon():
    for _ in range(10):
        timmy.fd(100)
        timmy.left(36)


def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        timmy.fd(100)
        timmy.right(angle)

    for sides in range(3, 11):
        draw_shape(sides)
        timmy.color(random.choice(colors))


def random_walk():
    timmy.width(15)
    for _ in range(500):
        angle = random.choice(angles)
        timmy.setheading(angle)
        timmy.fd(100)
        timmy.color(random.choice(colors))


random_walk()
screen = Screen()
screen.exitonclick()