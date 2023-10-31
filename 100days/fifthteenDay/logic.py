from resources import *


# def check_sufficient_resources(drink_ingredients):
# 	for item in resources:
# 		if resources[item] > drink_ingredients['resources'][item]:
# 			print("Sorry, we can't make that right now.")
			

def insert_coins():
	quarters = float(input("How many quarters? > ")) * 0.25
	dimes = float(input("How many dimes > ")) * 0.10
	nickels = float(input("How many nickels > ")) * 0.05
	pennies = float(input("How many pennies? > ")) * 0.01
	profit =  round(quarters + dimes + nickels + pennies, 2)
	print(f"You have inserted ${profit}")
