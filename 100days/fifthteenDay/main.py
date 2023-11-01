from resources import *
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
	for item in resources:
		if resources[item] <= drink_resources['ingredients'][item]:
			return f"Sorry, we don't have enough {item}"


def insert_coins():
	quarters = float(input("How many quarters? > ")) * 0.25
	dimes = float(input("How many dimes > ")) * 0.10
	nickels = float(input("How many nickels > ")) * 0.05
	pennies = float(input("How many pennies? > ")) * 0.01
	profit =  round(quarters + dimes + nickels + pennies, 2)
	print(f"You have inserted ${profit}")


def check_transaction(money_import):
	global profit
	global user_input
	if profit == MENU[user_input]['cost']:
		profit += MENU[user_input]['cost']
	elif profit > MENU[user_input]['cost']:
		print("Sorry, that's not enough money. Money refounded.")
		

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
		print(f"Money: {profit}$")
		power_off = True
	else:
		drink = MENU[user_input]
		check_sufficient_resources(drink)
		if insert_coins() == True:
			check_transaction(profit)
