
user_input = input("What would you like? espresso/latte/cappuccino\n> ").lower()
power_off = False


def coffe_machine():
	global power_off

	milk = 1000
	water = 1000
	coffee = 500
	money = 0

	espresso_water = 50
	espresso_coffee = 18

	latte_water = 200
	latte_coffee = 24
	latte_milk = 150

	cappuccino_water = 250
	cappuccino_coffee = 24
	cappuccino_milk = 150

	if user_input == "off":
		power_off = True
	elif user_input == "report":
		print(f"Water: {water}ml")
		print(f"Milk: {milk}ml")
		print(f"Coffee: {coffee}g")
		print(f"Money: {money}$")
	elif user_input == "espresso":
		water -= espresso_water
		coffee -= espresso_coffee
	elif user_input == "latte":
		water -= latte_water
		coffee -= latte_coffee
		milk -= latte_milk
	elif user_input == "cappuccino":
		water -= cappuccino_water
		coffee -= cappuccino_coffee
		milk -= cappuccino_milk


	print(milk)
	print(water)
	print(coffee)
	print(money)
