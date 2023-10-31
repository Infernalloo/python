from resources import *


def check_sufficient_resources(drink_ingredients):
	for item in resources:
		if resources[item] > drink_ingredients['resources'][item]:
			print("Sorry, we can't make that right now.")