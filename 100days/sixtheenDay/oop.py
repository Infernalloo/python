# # object = Class()
# import turtle

# # created a variable called timmy
# # tapped into the turtle module
# # called the class Turtle()
# timmy = turtle.Turtle()

# from turtle import *

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkSeaGreen4")
# timmy.forward(100)

# screen = Screen()
# print(screen.canvheight)

# screen.exitonclick()

from prettytable import *

table = PrettyTable()
table.add_column("Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
