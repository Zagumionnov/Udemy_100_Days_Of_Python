
def start_game():
    step_one = input('Welcome to Treasure Island. Your mission is to find the treasure. Left or right? ')
    if step_one != 'left':
        return print('Fall into a hole. Game Over.')
    step_two = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')
    if step_two != 'wait':
        return print('Attacked by trout. Game Over.')
    step_three = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, on blue. Which colour do you choose? ')
    if step_three == 'red':
        print('Burned by fire. Game Over.')
    elif step_three == 'blue':
        print('Eaten by beasts. Game Over.')
    elif step_three == 'yellow':
        print('You Win!')
    else:
        print('Game Over.')


if __name__ == '__main__':
    start_game()
