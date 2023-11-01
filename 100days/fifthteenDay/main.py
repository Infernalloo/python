from resources import *
from logic import *
power_off = False

while not power_off:
	user_input = input("What do you want to drink? espresso/latte/cappuccino > ").lower()
	if user_input == "off":
		power_off = True
	elif user_input == "report":
		print(f"Water: {resources['water']}ml")
		print(f"Milk: {resources['milk']}ml")
		print(f"Coffee: {resources['coffee']}g")
		print(f"Money: {profit}$")
		power_off = True
	else:
		drink = MENU[user_input]
		print(drink)
		check_sufficient_resources(drink)
		insert_coins()
