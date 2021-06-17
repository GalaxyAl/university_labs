import sys
import random
from PyQt5 import QtWidgets
from card import Card
from deck import Deck


class MainSolitaire(QtWidgets.QWidget):
    SUITS = ["H", "H", "S", "S"]
    TYPES = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    START_DECK_SIZE = 6
    DECK_NUM = 8

    def __init__(self):
        super(MainSolitaire, self).__init__()
        self.total_cards = self.__generate_total_cards()
        self.decks = self.__generate_decks()

        self.__display_decks()

        self.setGeometry(800, 300, 1000, 400)
        self.show()

    def __generate_total_cards(self):
        total_cards = []
        for suit in self.SUITS:
            for card_type in self.TYPES:
                total_cards.append(Card(card_type, suit, parent=self))

        random.shuffle(total_cards)
        return total_cards

    def __generate_decks(self, handle_card_states=True):
        decks = set()
        for i in range(self.DECK_NUM):
            deck = Deck(self.total_cards[:self.START_DECK_SIZE])
            decks.add(deck)
            self.total_cards = self.total_cards[self.START_DECK_SIZE:]

            if handle_card_states:
                for card in deck.stack:
                    if card == deck.stack[-1]:
                        card.hidden = False

        return decks

    def __display_decks(self) -> None:
        horizontal_offset = 100
        vertical_offset = 15

        default_vertical_position = 100
        horizontal_position = 50

        current_vertical_position = default_vertical_position

        for deck in self.decks:
            horizontal_position += horizontal_offset
            for card in deck:
                card.move(horizontal_position, current_vertical_position)
                card.raise_()
                current_vertical_position += vertical_offset

            current_vertical_position = default_vertical_position

app = QtWidgets.QApplication(sys.argv)
window = MainSolitaire()
sys.exit(app.exec())
