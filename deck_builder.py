class Deck:
    def __init__(self):
        self.suits = ["hearts", "clubs", "diamonds", "spades"]
        self.face_cards = ["jack", "queen", "king", "ace"]

    def build_deck(self):
        for each in self.suits:
            for i in range(1, 11):
                card = Card(each, i)
            for face in self.face_cards:
                card = Card(each, face)

    def deck_storage(self, card):
        # linked list constructor
        pass
    


class Card:
    def __init__(self, suit=None, value=None):
        self.suit = suit
        self.value = value
        # linked list elements
        self.next = None
        self.prev = None

    def __str__(self):
        """Returns first letter of suit and value"""
        return str(self.suit[0]) + str(self.value)

    def set_prev(self, other):
        """Sets previous card value for linked list"""
        self.prev = other

    def set_next(self, other):
        """Sets next card value for linked list"""
        self.next = other

    def set_suit(self, suit):
        """Method for setting card suit"""
        self.suit = suit

    def set_value(self, value):
        """Method for setting card value"""
        self.value = value
