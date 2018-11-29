import random

random.seed(126)


class AbstractCard:
    def __init__(self, rank):
        self.rank = rank

    def _rank_to_str(self):
        if self.rank == 11:
            return 'J'
        if self.rank == 12:
            return 'Q'
        if self.rank == 13:
            return 'K'
        if self.rank == 14:
            return 'A'
        if self.rank == 15:
            return '*'
        return str(self.rank)

    def __gt__(self, other):
        return self.rank > other.rank


class Card(AbstractCard):
    # suit - h
    # rank 2-10, 11 - jack, 12 - queen, 13 - king, 14 - ace
    def __init__(self, suit, rank):
        super().__init__(rank)
        self.suit = suit

    suits = {
        'clubs': '♣',
        'diamonds': '♦',
        'hearts': '♥',
        'spades': '♠'}

    def __str__(self):
        return "{rank}{suit}".format(rank=self._rank_to_str(), suit=self.suits[self.suit])


class Jocker(AbstractCard):
    def __init__(self):
        super().__init__(15)

    def __str__(self):
        return "{rank}".format(rank=self._rank_to_str())


class Deck:
    def __init__(self):
        self.__the_cards = []

        for suit in Card.suits.keys():
            for rank in range(2, 15):
                self.__the_cards.append(Card(suit, rank))
        self.__the_cards.append(Jocker())
        self.__the_cards.append(Jocker())

        random.shuffle(self.__the_cards)

    def print_deck(self):
        for card in self.__the_cards:
            print(card)

    def get_card(self):
        return self.__the_cards.pop()


class Hand:
    def __init__(self, cards_count):
        self.__the_cards = []
        self.cards_count = cards_count

    def add_card(self, card):
        self.__the_cards.append(card)

    def sort_cards(self):
        self.__the_cards = sorted(self.__the_cards)

    def __str__(self):
        ret_str = ""
        for card in self.__the_cards:
            ret_str += " " + str(card)
        return ret_str


deck = Deck()

h1 = Hand(5)
h2 = Hand(5)

for i in range(h1.cards_count):
    h1.add_card(deck.get_card())

for i in range(h2.cards_count):
    h2.add_card(deck.get_card())

h1.sort_cards()
h2.sort_cards()

print("hand1", h1)
print("hand2", h2)

# deck.print_deck()
