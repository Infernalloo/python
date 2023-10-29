user_input = input("What would you like? espresso/latte/cappuccino\n> ").lower()
power_off = False
milk = 1000
water = 1000
coffee = 500
money = 0

if user_input == "off":
	power_off = True
elif user_input == "report":
	print(f"Water: {water}ml")
	print(f"Milk: {milk}ml")
	print(f"Coffee: {coffee}g")
	print(f"Money: {money}$")
