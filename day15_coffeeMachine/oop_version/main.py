#!/usr/bin/python3

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"what would you like? {menu.get_items()} \n").lower()
    print(f"[DEBUG] selected choice: {choice}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(f"[DEBUG] drink name: {drink.name}")
        print(f"[DEBUG] drink cost: {drink.cost}")
        print(f"[DEBUG] drink ingredients: {drink.ingredients}")
        can_make = coffee_maker.is_resource_sufficient(drink)
        print(f"[DEBUG] can make = {can_make}")
        if can_make == True:
            payment = money_machine.make_payment(drink.cost)
            print(f"[DEBUG] payment = {payment}")
        if payment == True:
            coffee_maker.make_coffee(drink)
            