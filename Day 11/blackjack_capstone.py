import random


def render_players_current_values(users_cards, computers_cards):
    print(f'Your cards: {users_cards}, current score: {sum(users_cards)}')
    print(f"Computer's first card: {computers_cards[0]}")


def render_players_final_values(users_cards, computers_cards):
    print(f'Your final hand: {users_cards}, final score: {sum(users_cards)}')
    print(f"Computer's final card: {computers_cards}, final score: {sum(computers_cards)}")


def take_a_card(players_cards, cards):
    players_cards.append(random.choice(cards))


def check_result(users_cards, computers_cards):
    user_cards_sum = sum(users_cards)
    computers_cards_sum = sum(computers_cards)
    if user_cards_sum == 21 and computers_cards_sum == 21:
        render_players_final_values(users_cards, computers_cards)
        print('Draw!')
        return True
    if user_cards_sum == 21 and computers_cards_sum < 21:
        render_players_final_values(users_cards, computers_cards)
        print('You win!')
        return True
    if user_cards_sum > 21:
        render_players_final_values(users_cards, computers_cards)
        print('You lose!')
        return True


def check_final_result(users_cards, computers_cards):
    user_cards_sum = sum(users_cards)
    computers_cards_sum = sum(computers_cards)
    if computers_cards_sum > 21:
        render_players_final_values(users_cards, computers_cards)
        print('You win!')
        return True
    if user_cards_sum > computers_cards_sum:
        render_players_final_values(users_cards, computers_cards)
        print('You win!')
        return True
    if user_cards_sum < computers_cards_sum:
        render_players_final_values(users_cards, computers_cards)
        print('You lose!')
        return True


def start_blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    users_cards = random.choices(cards, k=2)
    computers_cards = random.choices(cards, k=2)
    render_players_current_values(users_cards, computers_cards)
    if check_result(users_cards, computers_cards):
        return
    while input(f"Type 'y' to get another card, type 'n' to pass: ") != 'n' and sum(users_cards) < 21:
        take_a_card(users_cards, cards)
        render_players_current_values(users_cards, computers_cards)
        if check_result(users_cards, computers_cards):
            return
    while sum(computers_cards) < 17:
        take_a_card(computers_cards, cards)
    if check_final_result(users_cards, computers_cards):
        return True


if __name__ == "__main__":
    start_blackjack()
