from resources import *
power_off = False
profit = 0


def check_resources(drink_ingredients):
    for ingredient in MENU[drink_ingredients]:
        if drink_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, we don't have enough {ingredient}")

while not power_off:
    user_input = input("What do you want to drink? espresso/latte/cappuccino\n> ").lower()
    if user_input == "off":
        power_off = True
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: {profit}$")
    else:
        drink = MENU[user_input]
        print(drink)
        check_resources
