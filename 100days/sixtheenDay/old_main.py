def coffe_machine():
	user_input = input("What would you like? espresso/latte/cappuccino\n> ").lower()
	print("Insert money\n ")
	user_quarter = float(input("How many quarters? >"))
	user_dimes = float(input("How many dimes? >"))
	user_nickels = float(input("How many nickels? >"))
	user_pennies = float(input("How many pennies? >"))

	milk = 1000
	water = 1000
	coffee = 500
	money = 0

	quarter = 0.25
	dimes = 0.10
	nickels = 0.05
	pennies = 0.01

	espresso_water = 50
	espresso_coffee = 18

	latte_water = 200
	latte_coffee = 24
	latte_milk = 150

	cappuccino_water = 250
	cappuccino_coffee = 24
	cappuccino_milk = 150

	if user_input == "off":
		print("The machine is turning off...")
		return
	elif user_input == "report":
		print(f"Water: {water}ml")
		print(f"Milk: {milk}ml")
		print(f"Coffee: {coffee}g")
		print(f"Money: {money}$")
	elif user_input == "espresso":
		if water < espresso_water:
			print("Sorry, there is not enough water")
			return
		elif coffee < espresso_coffee:
			print("Sorry, there is not enough coffee")
			return
		water -= espresso_water
		coffee -= espresso_coffee
	elif user_input == "latte":
		if water < latte_water:
			print("Sorry, there is not enough water")
			return
		elif coffee < latte_coffee:
			print("Sorry, there is not enough coffee")
			return
		elif milk < latte_milk:
			print("Sorry, there is not enough milk")
			return
		water -= latte_water
		coffee -= latte_coffee
		milk -= latte_milk
	elif user_input == "cappuccino":
		if water < cappuccino_water:
			print("Sorry, there is not enough water")
			return
		elif coffee < cappuccino_coffee:
			print("Sorry, there is not enough coffee")
			return
		elif milk < cappuccino_milk:
			print("Sorry, there is not enough milk")
			return
		water -= cappuccino_water
		coffee -= cappuccino_coffee
		milk -= cappuccino_milk
	else:
		print("Did you type chose the correct thing?")
		return

	if user_input == "espresso":
		print("Here is your espresso. Enjoy!")
	elif user_input == "latte":
		print("Here is your latte. Enjoy!")
	elif user_input == "cappuccino":
		print("Here is you cappuccino. Enjoy! ")


coffe_machine()
