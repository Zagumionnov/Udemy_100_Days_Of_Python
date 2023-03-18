
def calculate_tips():
    print('Welcome to the tip calculator.')
    total_bill = float(input('What was the total bill? '))
    tip_percentage = float(input('What percentage tip would you like to give? '))
    people_count = int(input('How many people to split the bill? '))
    return print(round((total_bill + total_bill * tip_percentage / 100) / people_count, 2))


if __name__ == '__main__':
    calculate_tips()
