import random

from game_data import data


def choose_heroes():
    a = b = True
    while a == b:
        a = random.choice(data)
        b = random.choice(data)
    return a, b


def pick_winner(hero_a, hero_b):
    return hero_a if hero_a['follower_count'] == max([hero_a['follower_count'], hero_b['follower_count']]) else hero_b


def check_answer(user_answer, correct_answer, score):
    if user_answer != correct_answer['mark']:
        print(f"Sorry, that's wrong. Final score: {score}")
        return True


def start_game():
    score = 0
    while True:
        hero_a, hero_b = choose_heroes()
        hero_a['mark'] = 'A'
        hero_b['mark'] = 'B'
        correct_answer = pick_winner(hero_a, hero_b)
        print(f"Compare A: {hero_a['name']}, {hero_a['description']}, {hero_a['country']}")
        print(f"Against B: {hero_b['name']}, {hero_b['description']}, {hero_b['country']}")
        if check_answer(input("Who has more instagram follower? Type 'A' or 'B': "), correct_answer, score):
            return
        score += 1
        print(f"You're right! Current score: {score}")


if __name__ == '__main__':
    start_game()
