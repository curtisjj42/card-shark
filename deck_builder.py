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
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
