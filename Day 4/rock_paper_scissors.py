import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


def render_by_choice(choice):
    if choice == 0:
        return rock
    elif choice == 1:
        return scissors
    else:
        return paper


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Draw'
    elif (
            (user_choice == 0 and computer_choice == 1) or
            (user_choice == 1 and computer_choice == 2) or
            (user_choice == 2 and computer_choice == 0)
    ):
        return 'You win!'
    else:
        return 'You lose'


def start_game():
    print('Welcome to Rock-Paper-Scissors game!')
    user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Scissors or 2 Paper. '))
    computer_choice = random.randint(0, 2)
    print('User choice:\n', render_by_choice(user_choice))
    print('Computer choice:\n', render_by_choice(computer_choice))
    print(determine_winner(user_choice, computer_choice))


if __name__ == '__main__':
    start_game()
