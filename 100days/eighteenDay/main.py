# import colorgram
import turtle
import random

# colors = colorgram.extract('image.jpg', 15)
# color_tuples = []
# for i in colors:
#     red = i.rgb.r
#     green = i.rgb.g
#     blue = i.rgb.b
#     rgb_value = (red, green, blue)
#     color_tuples.append(rgb_value)
#
# print(color_tuples)

colors_list = [(239, 241, 245), (208, 160, 111), (188, 168, 17), (32, 105, 142), (173, 82, 29), (13, 51, 84),
               (142, 174, 195), (217, 209, 123), (158, 23, 13), (195, 142, 157), (144, 68, 102), (94, 161, 80)]
timmy = turtle.Turtle()
turtle.colormode(255)
timmy.shape("turtle")


def draw_line():
    for _ in range(10):
        timmy.dot(20, random.choice(colors_list))
        timmy.fd(50)


for _ in range(5):
    draw_line()
    timmy.setheading(90)
    timmy.fd(50)
    timmy.setheading(180)
    draw_line()

screen = turtle.Screen()
screen.exitonclick()
