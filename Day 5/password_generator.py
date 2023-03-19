import random
import string


def generate_password(letters, numbers, punctuation):
    letters_string = [random.choice(string.ascii_letters) for _ in range(letters)]
    numbers_string = [random.choice(string.digits) for _ in range(numbers)]
    punctuation_string = [random.choice(string.punctuation) for _ in range(punctuation)]
    password_list = letters_string + numbers_string + punctuation_string
    random.shuffle(password_list)

    return ''.join(password_list)


def start_generator():
    letters = int(input('How many letters would you like in your password? '))
    numbers = int(input('How many numbers would you like? '))
    punctuation = int(input('How many synbols would you like? '))
    return print('Here is your password: ' + generate_password(letters, numbers, punctuation))


if __name__ == '__main__':
    start_generator()
