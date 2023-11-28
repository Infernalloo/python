power_off = False

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def check_sufficient_resources(drink_resources):
	for item in drink_resources:
		if resources[item] < drink_resources[item]:
			print(f"Sorry, there is not enough {item}.")
			return False
	return True


def insert_coins():
	quarters = float(input("How many quarters? > ")) * 0.25
	dimes = float(input("How many dimes > ")) * 0.10
	nickels = float(input("How many nickels > ")) * 0.05
	pennies = float(input("How many pennies? > ")) * 0.01
	profit =  round(quarters + dimes + nickels + pennies, 2)
	print(f"You have inserted ${profit}")
	return profit


def transaction_check(payment_input, drink_cost):
	global profit
	change = round(payment_input - drink_cost, 2)
	print(f"Here is ${change} in change.")
	if payment_input >= drink_cost:
		profit += payment_input - change
		return True
	else:
		print("Sorry, that is not enough money. Money refounded.")
		return False


def make_coffee(drink_name, order_ingredients):
	for item in order_ingredients:
		resources[item] -= order_ingredients[item]
	print(f"Here is your {drink_name}")


while not power_off:
	print(f"Espresso: {MENU['espresso']['cost']}$")
	print(f"Latte: {MENU['latte']['cost']}$")
	print(f"Cappuccino: {MENU['cappuccino']['cost']}$")
	user_input = input("What do you want to drink? > ").lower()
	if user_input == "off":
		power_off = True
	elif user_input == "report":
		print(f"Water: {resources['water']}ml")
		print(f"Milk: {resources['milk']}ml")
		print(f"Coffee: {resources['coffee']}g")
		print(f"Money: {round(profit, 2)}$")
	else:
		drink = MENU[user_input]
		if check_sufficient_resources(drink['ingredients']):
			payment = insert_coins()
			if transaction_check(payment, drink['cost']):
				make_coffee(user_input, drink['ingredients'])

