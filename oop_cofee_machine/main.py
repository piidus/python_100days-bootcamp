from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

order = print("What would you like? \n(espresso/latte/cappuccino):")
is_on = True
while is_on:
    time.sleep(1)
    if order == "off":
        is_on = False
        print(order)
    else:
        print(order)