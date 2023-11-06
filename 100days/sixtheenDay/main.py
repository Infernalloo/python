from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_item = MenuItem()
menu = Menu()
power_on = True

while power_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        coffee_maker.is_resource_sufficient(drink)