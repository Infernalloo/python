# OOP
# From a Class you can make multiple objects
# Object = Class
# car    = CarBlueprint()
# Object --> Attributes (variables for object)
# Object --> Methods (functions for object)
# Do differentiate between classes and functions
# the classes are writen in PascalCase
#
# from turtle import *
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkSeaGreen4")
# timmy.forward(100)
#
# # object.attribute
# my_screen = Screen()
# print(my_screen.canvheight)
#
# # object.method
# my_screen.exitonclick()

from prettytable import *
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
