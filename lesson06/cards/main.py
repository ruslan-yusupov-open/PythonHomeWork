import random


class Card:
    # suit - h
    # rank 2-10, 11 - jack, 12 - queen, 13 - king, 14 - ace
    suits = {
        'clubs': '♣',
        'diamonds': '♦',
        'hearts': '♥',
        'spades': '♠'}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __rank_to_str(self):
        if self.rank == 11:
            return 'J'
        if self.rank == 12:
            return 'Q'
        if self.rank == 13:
            return 'K'
        if self.rank == 14:
            return 'A'
        return str(self.rank)

    def __str__(self):
        return "{rank}{suit}".format(rank=self.__rank_to_str(), suit=self.suits[self.suit])


class Deck:
    def __init__(self):
        self.__the_cards = []

        for suit in Card.suits.keys():
            for rank in range(2, 15):
                self.__the_cards.append(Card(suit, rank))

        random.shuffle(self.__the_cards)

    def print_deck(self):
        for card in self.__the_cards:
            print(card)


