import machine_data


def get_order():
    while True:
        choice = input('What would you like? (espresso/latte/cappuccino): ')
        if choice in ['espresso', 'latte', 'cappuccino', 'report']:
            return choice
        print('Unknown command! Try again.')


def process_order(order):
    for ingredient in machine_data.MENU[order]['ingredients'].keys():
        if machine_data.MENU[order]['ingredients'][ingredient] > machine_data.resources[ingredient]:
            return False, ingredient
    return True, machine_data.MENU[order]['cost']


def process_payment(coffee_price, machine_data):
    quarters = float(input('Please insert coins.\nHow many quarters? ')) * 0.25
    dimes = float(input('How many dimes? ')) * 0.10
    nickels = float(input('How many nickels? ')) * 0.05
    pennies = float(input('How many pennies? ')) * 0.01
    total = quarters + dimes + nickels + pennies
    if coffee_price > total:
        print("Sorry that's not enogh money. Money refunded.")
        return False
    machine_data.profit += coffee_price
    print(f"Here is {round(total - coffee_price)}$ in change.")
    return True


def making_coffee(order, machine_data):
    for ingredient in machine_data.MENU[order]['ingredients'].keys():
        machine_data.resources[ingredient] -= machine_data.MENU[order]['ingredients'][ingredient]


def coffee_machine(machine_data):
    while True:
        order = get_order()
        if order == 'report':
            print(machine_data.resources)
            continue
        available, data = process_order(order)
        if not available:
            print(f'Sorry there is not enough {data}.')
            continue
        if not process_payment(data, machine_data):
            continue
        making_coffee(order, machine_data)
        print(f'Here is your {order}. Enjoy!')


if __name__ == '__main__':
    coffee_machine(machine_data)
