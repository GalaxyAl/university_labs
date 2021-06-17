import random

# from singleton import Singleton
from card import Card
# from deck import Deck


class Board:
    """
    Main game class.

    Represents solitaire 'board' class that contains all required constant values, states and behaviours
    (in the future will be added). Board is an embodiment of a GameManager so it uses singleton as a metaclass.
    Nowadays (15.02.2021) class allows to generate decks.
    """
    SUITS = {"H", "D", "C", "S"}
    TYPES = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    START_DECK_SIZE = 6
    DECK_NUM = 8

    TotalCards = []
    for suit in SUITS:
        for card_type in TYPES:
            TotalCards.append(Card(card_type, suit))

    random.shuffle(TotalCards)

    def __init__(self):
        self.decks = set()
        self.__generate_decks()

    def __generate_decks(self):
        for _ in range(self.DECK_NUM):
            deck_card_stack = random.sample(self.TotalCards, k=self.START_DECK_SIZE)

            # self.decks.add(Deck(deck_card_stack))
            self.TotalCards = list(set(self.TotalCards) - set(deck_card_stack))
            # Remove values from total card stack in that way as the current approach is quite fast
            # (providing to some stackoverflow post).

    def move_card(self):
        pass

    # def __str__(self):
        # return "Decks:\n\n {}".format('\n\n'.join([deck.__str__() for deck in self.decks]))
