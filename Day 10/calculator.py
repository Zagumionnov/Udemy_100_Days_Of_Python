
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 + n2


def devide(n1, n2):
    return n1 + n2


def start_calculator():
    n1 = float(input("What's the first number?: "))
    n2 = float(input("What's the second number?: "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    operations = {'+': add, '-': subtract, '*': multiply, '/': devide}
    print(f'{n1} {operation} {n2} = {operations[operation](n1, n2)}')


if __name__ == '__main__':
    start_calculator()
