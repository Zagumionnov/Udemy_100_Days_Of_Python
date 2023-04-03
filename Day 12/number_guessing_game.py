import random


def check_answer(number, computer_number):
    if number == computer_number:
        print(f"You got it! The answer was {computer_number}")
        return True
    if number > computer_number:
        print('Too high.\nGuess again.')
    if number < computer_number:
        print('Too low.\nGuess again.')


def start_game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 5 if difficulty == 'hard' else 10
    computer_number = random.randint(1, 100)
    for _ in range(attempts):
        print(f"You have {attempts} attempts remaining to guess the number.")
        attempts -= 1
        if check_answer(int(input('Make a guess: ')), computer_number):
            return
    print(f"You lose! The answer was {computer_number}")


if __name__ == '__main__':
    start_game()
