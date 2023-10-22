# Scope
enemies = 1
def increase_enemies() :
    enemies = 2
    print(f"enemies inside the function: {enemies}")

increase_enemies()
print(f"enemies outside the function: {enemies}")

# Local scope
# the variable potion_strength is available
# only inside the function
# can't print outside the function
def drink_potion() :
    potion_strength = 2
    print(potion_strength)
# gives error because is local scope
# print(potion_strength)

# Global scope
# the variable can be used inside or 
# outside the function
player_health = 10
def drink_potion2() :
    player_health = 2
    print(player_health)
print(player_health)

# There is no block scope in python
# if the variable is created inside a
# block wiht indentatin and a semicolon
# it's global scope, as below
game_level = 3
enemies = ["skeleton", "zombie", "alien"]
if game_level < 5 :
    new_enemy = enemies[0]
print(new_enemy)

# Modify a global variable
# inside the function declare the variable with 
# the "global" keyword before
# enemies = 1
# def increase_enemies() :
#     global enemies
#     enemies += 1

# Not recommended to use the above

# Global constants
# naming convention is to make it all uppercase
# PI = 3.14159