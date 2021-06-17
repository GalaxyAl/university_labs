from abc import ABC, abstractmethod


class ICard(ABC):
    """
    Abstract Card class.

    Base abstract class used for creating cards, based on this one.
    """
    def __init__(self, card_type, suit):

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
