"""
Created by Oleksii Liaskovskyi, CS 19.
"""

import random
from abc import ABC, abstractmethod


class Singleton(type):
    """
    Metaclass.

    Used for applying singleton pattern for an exact classes.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ICard(ABC):
    """
    Abstract Card class.

    Base abstract class used for creating cards, based on this one.
    """
    def __init__(self, suit, card_type):

        """
        :param suit: represents the card suit
        :param card_type: represents the card type
        """

        self.suit = suit
        self.type = card_type
        self.hidden_name = "---"
        self.name = f"{self.type} {self.suit}"

    @abstractmethod
    def stackable(self, other_card):
        pass

    def __str__(self):
        return f"Card name: {self.name}"


class IDeck(ABC):
    """
    Abstract Deck class.

    Base abstract class used for creating decks.
    """
    @abstractmethod
    def add_to_stack(self, amount, cards):
        pass

    @abstractmethod
    def remove_from_stack(self, card):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass


class Card(ICard):
    """
    Play card class.

    Inherits the base ICard abstract class, contains playing card states.
    """
    def stackable(self, other_card):
        if self.suit == other_card.suit:
            print("Stackable")


class Deck(IDeck):
    """
    Card deck class.

    Class-iterator. Includes functionality for playing deck. Nowadays (15.02.2021) Deck class allows to add cards
    to deck stack and remove them.
    """
    def __init__(self, init_amount_cards, total_cards):
        """

        :param init_amount_cards:
        :param total_cards:
        """
        self.stack = []
        self.add_to_stack(init_amount_cards, total_cards)

    def add_to_stack(self, amount, cards):
        for i in range(amount):
            random_card = random.choice(list(cards))
            self.stack.append(random_card)
            cards.remove(random_card)

    def remove_from_stack(self, card):
        self.stack.remove(card)

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx < len(self.stack):
            card = self.stack[self.idx]
            self.idx += 1
            return card
        else:
            raise StopIteration

    def __str__(self):
        return "\n".join([c.name if c == list(self.stack)[-1] else c.hidden_name
                          for c in self.stack])


class Board(metaclass=Singleton):
    """
    Main game class.

    Represents solitaire 'board' class that contains all required constant values, states and behaviours
    (in the future will be added). Board is an embodiment of a GameManager so it uses singleton as a metaclass.
    Nowadays (15.02.2021) class allows to generate decks.
    """
    SUITS = {"Heart", "Diamond", "Club", "Spade"}
    TYPES = {2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"}
    START_DECK_SIZE = 6

    TotalCards = set()
    for suit in SUITS:
        for card_type in TYPES:
            TotalCards.add(Card(card_type, suit))

    def __init__(self):
        self.deck_num = 8
        self.decks = set()
        self.__generate_decks()

    def __generate_decks(self):
        for i in range(self.deck_num):
            self.decks.add(Deck(self.START_DECK_SIZE, self.TotalCards))

    def move_card(self):
        pass

    def __str__(self):
        return "Decks:\n\n {}".format('\n\n'.join([deck.__str__() for deck in self.decks]))


if __name__ == "__main__":
    board = Board()
    print(board)

