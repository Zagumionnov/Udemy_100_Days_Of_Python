import random

from hangman_state import *
from words import words


def generate_game_logo():
    return """
    888                                                           
    888                                                           
    888                                                           
    88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
    888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
    888  888.d888888888  888888  888888  888  888.d888888888  888 
    888  888888  888888  888Y88b 888888  888  888888  888888  888 
    888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                                 888                              
                            Y8b d88P                              
                             "Y88P"    """


def generate_blanks(word):
    return ['_' for _ in range(len(word))]


def start_game():
    print(generate_game_logo())

    hangman_state = iter([one, two, three, four, five])
    word = random.choice(words).casefold()
    print(word)
    blanks_list = generate_blanks(word)

    while '_' in blanks_list:
        print(''.join(blanks_list))
        letter = input('Guess a letter: ')
        if letter not in word:
            state = next(hangman_state)
            print(state)
            if state == five:
                print('Game over')
                break
            continue
        for idx, val in enumerate(word):
            if letter == val:
                blanks_list[idx] = letter
        if '_' not in blanks_list:
            print(word)
            print('You win!')


if __name__ == '__main__':
    start_game()
