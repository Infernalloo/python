# Attributes: a variable associated with an object
# Methods: a function associated with an object
# From a class (blueprint) we can create more objects

from turtle import *
# obj = class()
jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("DarkSeaGreen4")
jimmy.forward(100)

screen = Screen()
#  obj.attribute
screen.canvheight = 500
screen.canvwidth = 500
#  obj.method()
screen.exitonclick()