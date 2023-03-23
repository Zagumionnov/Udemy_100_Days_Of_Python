import os


def start_secret_auction():
    new_bidder = True
    bidders = {}
    while new_bidder:
        bidder_name = input('What is your name?: ')
        bidders[bidder_name] = int(input('What is your bid?: $'))
        new_bidder = True if input("Are there any other bidders?: Type 'yes' or no.") == 'yes' else False
        if new_bidder:
            os.system('clear')
    winner = ''
    value = 0
    for name in bidders:
        if bidders[name] >= value:
            winner = name
            value = bidders[name]
    print(f'The winner is {winner} with a bid ${value}.')


if __name__ == '__main__':
    start_secret_auction()
