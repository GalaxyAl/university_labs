from abstract_deck import IDeck


class Deck(IDeck):
    """
    Card deck class.

    Class-iterator. Includes functionality for playing deck. Nowadays (15.02.2021) Deck class allows to add cards
    to deck stack and remove them.
    """
    def __init__(self, stack):
        """
        :param stack:
        """
        self.stack = stack

    # def add_to_stack(self, amount, cards):
    #     for i in range(amount):
    #         random_card = random.choice(list(cards))
    #         self.stack.append(random_card)
    #         cards.remove(random_card)
    #
    # def remove_from_stack(self, card):
    #     self.stack.remove(card)

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
