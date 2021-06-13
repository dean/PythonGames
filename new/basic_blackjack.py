import random


FACE_CARDS = ['Jack', 'Queen', 'King', 'Ace']
def bold(text):
    return f'\x1b[1m{text}\x1b[0m'


class Card():
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def __repr__(self):
        return str(self)

    def __str__(self):
        return bold(f'{self.name} of {self.suit}')


class Deck():
    def __init__(self):
        self.cards = self.new_deck()

    def new_deck(self, shuffle=True):
        cards = []
        for value in range(2, 15):
            for suit in ['Clubs', 'Spades', 'Hearts', 'Diamonds']:
                if value > 10:
                    _value = 11 if FACE_CARDS[value - 11] == "Ace" else 10
                    cards.append(Card(FACE_CARDS[value - 11], suit, _value))
                else:
                    cards.append(Card(value, suit, value))
        if shuffle:
            random.shuffle(cards)
        return cards

    def top_card(self):
        return self.cards.pop()


class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []

    def clear_hand(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def print_blackjack_hand(self):
        hand_string = f'[{bold(self.name)}] ' + bold(' '.join([f'{i+1}. {self.cards[i]}' for i in range(len(self.cards))]))
        values = self.blackjack_hand_values()
        hand_string += f' (Value: {bold(values[0])})' if len(values) == 1 else ' (Values: ' + ', '.join(sorted(map(bold, values))) + ')'
        print(hand_string)

    def blackjack_hand_values(self):
        values = [sum([card.value for card in self.cards])]
        num_aces = [card for card in self.cards if card.name == "Ace"]
        for i in range(len(num_aces)):
            values.append(values[0] - 10 * (i + 1) )
        return values



def play():
    dealer = Player('Dealer')
    human = Player(input('What is your name?:').strip())

    while True:
        dealer.clear_hand()
        human.clear_hand()
        deck = Deck()

        # Deal
        for _ in range(2):
            dealer.add_card(deck.top_card())
            human.add_card(deck.top_card())

        dealer.print_blackjack_hand()
        human.print_blackjack_hand()

        hit = True
        while hit and any([value < 21 for value in human.blackjack_hand_values()]):
            hit = input('Hit[y/N]?: ').startswith('y')
            if hit:
                human.add_card(deck.top_card())

        if all([value > 21 for value in human.blackjack_hand_values()]):
            print(f'{human.name} BUSTED! Starting new round...')
            continue

        while hit:
            hit = not any([value > 16 for value in dealer.blackjack_hand_values()])
            if hit:
                Dealer.add_card(deck.top_card())

        if all([value > 21 for value in dealer.blackjack_hand_values()]):
            print(f'{dealer.name} BUSTED! Starting new round...')

        player_highest_nonbust_hand = max([value for value in human.blackjack_hand_values() if value < 21])
        dealer_highest_nonbust_hand = max([value for value in dealer.blackjack_hand_values() if value < 21])
        if player_highest_nonbust_hand > dealer_highest_nonbust_hand:
            print('f{player.name} WON! Starting new round...')
        elif dealer_highest_nonbust_hand > player_highest_nonbust_hand:
            print('f{dealer.name} WON! Starting new round...')
        else:
            print('TIE! Starting new round...')


if __name__ == '__main__':
    play()
