from resources import *
power_off = False


def check_resources(order_ingridients):
	for ingredient in order_ingridients:
		if resources[ingredient] < order_ingridients[ingredient]:
			print("Sorry, we don't have enough ingredients to make the drink.")


while not power_off:
	user_choice = input("What would you like to drink? espresso/latte/cappuccino\n> ")
	if user_choice == "off":
		print("The machine is powering off...")
		power_off = True
	elif user_choice == "report":
		print(f"Water: {resources['water']}ml")
		print(f"Coffee: {resources['coffee']}g")
		print(f"Milk: {resources['milk']}ml")
		print(f"Money: {profit}$")
	else:
		drink = MENU[user_choice]
		check_resources(drink["ingredients"])
