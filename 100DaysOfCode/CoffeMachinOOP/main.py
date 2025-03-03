from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker1 = CoffeeMaker()
money_machine1 = MoneyMachine()
menu1 = Menu()


costumer_command = input(f" What would you like ({menu1.get_items()})?: ").lower()
while not(costumer_command == "off"):
    if costumer_command == "report":
        coffee_maker1.report()
        money_machine1.report()
    else:
        wanted_drink = menu1.find_drink(costumer_command)
        if coffee_maker1.is_resource_sufficient(wanted_drink):
            if money_machine1.make_payment(wanted_drink.cost):
                coffee_maker1.make_coffee(wanted_drink)

    costumer_command = input(f" What would you like ({menu1.get_items()})?: ").lower()
