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

colors_list = [(208, 160, 111), (188, 168, 17), (32, 105, 142), (173, 82, 29), (13, 51, 84),
               (142, 174, 195), (217, 209, 123), (158, 23, 13), (195, 142, 157), (144, 68, 102), (94, 161, 80)]
timmy = turtle.Turtle()
turtle.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")
timmy.penup()
timmy.ht()
num_dots = 100

timmy.setheading(225)
timmy.fd(300)
timmy.setheading(0)

for dot_count in range(1, num_dots + 1):
    timmy.dot(20, random.choice(colors_list))
    timmy.fd(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.fd(50)
        timmy.setheading(180)
        timmy.fd(500)
        timmy.seth(0)

screen = turtle.Screen()
screen.exitonclick()
