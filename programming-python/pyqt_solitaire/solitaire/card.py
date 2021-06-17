from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui


class Card(QLabel):
    """
    Play card class.

    Inherits the base ICard abstract class, contains playing card states.
    """
    def __init__(self, card_type, suit, parent=None):
        super().__init__(parent)
        self.suit = suit
        self.type = card_type
        self.hidden = True
        self.name = f"{self.type}{self.suit}"

    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, new_status):
        self._hidden = new_status
        self.setup_img()

    def stackable(self, other_card):
        if self.suit == other_card.suit:
            print("Stackable")

    def setup_img(self):
        pixmap = QtGui.QPixmap("cards/hidden.png") if self.hidden else QtGui.QPixmap(f"cards/{self.name}.png")
        self.setPixmap(pixmap)
