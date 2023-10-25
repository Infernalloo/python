from coffe import resources
from coffe import MENU

selected_coffee = ""
close_machine = False


def coffe_dispenser():
    global selected_coffee
    global close_machine
    current_water = resources["water"]
    current_milk = resources["milk"]
    current_coffee = resources["coffee"]

    user_input = input("What would you like? (Espresso/Latte/Cappuccino)").lower()
    if user_input == "espresso":
        selected_coffee = MENU["espresso"]
        current_water -= MENU["espresso"]["ingredients"]["water"]
        current_coffee -= MENU["espresso"]["ingredients"]["coffee"]
    elif user_input == "latte":
        selected_coffee = MENU["latte"]
        current_water -= MENU["latte"]["ingredients"]["water"]
        current_coffee -= MENU["latte"]["ingredients"]["coffee"]
        current_milk -= MENU["latte"]["ingredients"]["milk"]
    elif user_input == "cappuccino":
        selected_coffee = MENU["cappuccino"]
        current_water -= MENU["cappuccino"]["ingredients"]["water"]
        current_coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
        current_milk -= MENU["cappuccino"]["ingredients"]["milk"]
    elif user_input == "off":
        close_machine = True
    elif user_input == "report":
        print(f"Water: {current_water}")
        print(f"Milk: {current_milk}")
        print(f"Coffee: {current_coffee}")


while not close_machine:
    coffe_dispenser()
