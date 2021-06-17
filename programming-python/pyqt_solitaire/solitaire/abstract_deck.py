from abc import ABC, abstractmethod


class IDeck(ABC):
    """
    Abstract Deck class.

    Base abstract class used for creating decks.
    """
    # @abstractmethod
    # def add_to_stack(self, amount, cards):
    #     pass
    #
    # @abstractmethod
    # def remove_from_stack(self, card):
    #     pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass
