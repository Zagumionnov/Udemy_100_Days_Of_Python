from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def get_order():
    while True:
        choice = input('What would you like? (espresso/latte/cappuccino): ')
        if choice in ['espresso', 'latte', 'cappuccino', 'report']:
            return choice
        print('Unknown command! Try again.')


def start_coffee_machine():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    while True:
        order = get_order()
        if order == 'report':
            coffee_maker.report()
            money_machine.report()
            continue
        drink = menu.find_drink(order)
        if not coffee_maker.is_resource_sufficient(drink):
            continue
        if not money_machine.make_payment(drink.cost):
            continue
        coffee_maker.make_coffee(drink)

if __name__ == '__main__':
    start_coffee_machine()
