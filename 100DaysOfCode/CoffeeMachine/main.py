from data import MENU
from data import resources


def print_report(money_in_machine):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"Money: {money_in_machine}$")


def check_enough_resources(costumer_drink):
    if costumer_drink == 'espresso':
        if resources['water'] < MENU['espresso']['ingredients']['water']:
            print("Sorry there is not enough Water")
            return False
        elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
            print("Sorry there is not enough Coffee")
            return False
        else:
            return True
    elif costumer_drink == 'latte':
        if resources['water'] < MENU['latte']['ingredients']['water']:
            print("Sorry there is not enough Water")
            return False
        elif resources['milk'] < MENU['latte']['ingredients']['milk']:
            print("Sorry there is not enough Milk")
            return False
        elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
            print("Sorry there is not enough Coffee")
            return False
        else:
            return True
    else:
        if resources['water'] < MENU['cappuccino']['ingredients']['water']:
            print("Sorry there is not enough Water")
            return False
        elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
            print("Sorry there is not enough Milk")
            return False
        elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
            print("Sorry there is not enough Coffee")
            return False
        else:
            return True


def calculate_costumer_coins(costumer_coins):
    return round((0.25 * costumer_coins['quarters'])
                 + (0.1 * costumer_coins['dimes']) +
                 (0.05 * costumer_coins['nickles']) +
                 (0.01 * costumer_coins['pennies']), 2)


def process_coins(costumer_drink):
    print("Please insert coins.")
    costumer_coins = {'quarters': float(input("How many quarters?: ")), 'dimes': float(input("How many dimes?: ")),
                      'nickles': float(input("How many nickles?: ")), 'pennies': float(input("How many pennies?: "))}

    costumer_total = calculate_costumer_coins(costumer_coins)
    if costumer_total < MENU[costumer_drink]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(costumer_total - MENU[costumer_drink]['cost'],2)
        print(f"Here is ${change} in change")
        return True


def coffe_machine():
    current_money = 0

    costumer_command = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    while not(costumer_command == "off"):
        if costumer_command == "report":
            print_report(current_money)
        else:
            if check_enough_resources(costumer_command):
                if process_coins(costumer_command):
                    current_money += MENU[costumer_command]['cost']
                    print(f"Here is your {costumer_command} ☕️. Enjoy!")

        costumer_command = input(" What would you like? (espresso/latte/cappuccino): ").lower()


coffe_machine()
