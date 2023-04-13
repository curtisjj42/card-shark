class Deck:
    def __init__(self, jokers = False):
        # make each suit names and face card names lowercase for later processing
        self.suits = ["hearts", "clubs", "diamonds", "spades"]
        self.face_cards = ["jack", "queen", "king", "ace"]
        # using jokers?
        self.jokers = jokers
        # top and bottom of deck, occupied by a card
        self.bottom = None
        self.top = None

        # list to hold all cards
        self.cards = []
        # create deck
        self.build_deck()

    def build_deck(self):
        # go through each suit
        for each in self.suits:
            # go thru cards 2-top spot (standard case is 10)
            for i in range(2, 11):
                # create card
                card = Card(each, i)
                # add card to list of cards
                self.cards.append(card)
            # create jack, queen, king if needed - check if face cards is not None
            for face in self.face_cards:
                card = Card(each, face)
                self.cards.append(card)

        self.deck_storage()

    def deck_storage(self):
        """
        Iterates through internal cardholder list, linked each card sequentially
        :param cards: instance of the Card class
        :return: None
        """

        for i in range(len(self.cards)):
            # first card
            if i == 0:
                # make first card bottom of deck
                self.bottom = self.cards[i]
                self.cards[i].prev = None
                self.cards[i].next = self.cards[i+1]
            # last card
            elif i == len(self.cards)-1:
                self.top = self.cards[i]
                self.cards[i].prev = self.cards[i-1]
                self.cards[i].next = None
            # rest of the cards
            else:
                self.cards[i].prev = self.cards[i-1]
                self.cards[i].next = self.cards[i+1]


class Card:
    def __init__(self, suit=None, name=None):
        self.suit = suit
        self.name = name
        # linked list elements
        self.next = None
        self.prev = None

    def __str__(self):
        """Returns first letter of suit and value"""
        return str(self.suit[0]) + str(self.name)

    def set_prev(self, other):
        """Sets previous card value for linked list"""
        self.prev = other

    def set_next(self, other):
        """Sets next card value for linked list"""
        self.next = other

    def set_suit(self, suit):
        """Method for setting card suit"""
        self.suit = suit

    def set_name(self, name):
        """Method for setting card value"""
        self.name = name
