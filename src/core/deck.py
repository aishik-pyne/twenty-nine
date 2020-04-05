import random
SUITES = ['H', 'D', 'S', 'C']
NUMBERS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Deck:
    cards = []

    def __init__(self, suites, numbers):
        self.cards = []
        for suit in suites:
            for number in numbers:
                self.cards.append("{}{}".format(suit, number))

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards = sorted(self.cards, key=lambda x: (
            SUITES.index(x[0]), NUMBERS.index(x[1:])))

    def aquire(self, cards):
        self.cards.extend(cards)
        return

    def deal(self, count):
        if count < len(self.cards):
            cards = self.cards[:count]
            self.cards = self.cards[count:]
            return cards
        else:
            raise KeyError("Not sufficient cards in the deck")

    @staticmethod
    def create_empty_deck():
        deck = Deck(suites=[], numbers=[])
        return deck

    @staticmethod
    def create_shuffled_deck(suites=SUITES, numbers=NUMBERS):
        deck = Deck(suites=SUITES, numbers=NUMBERS)
        deck.shuffle()
        return deck
