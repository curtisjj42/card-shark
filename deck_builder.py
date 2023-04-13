class Deck:
    def __init__(self,
                 suits = ["hearts", "clubs", "diamonds", "spades"],
                 face_cards = ["jack", "queen", "king", "ace"],
                 top_spot = 10,
                 jokers = False):
        # make each suit names and face card names lowercase for later processing
        self.suits = [each.lower() for each in suits]
        self.face_cards = [each.lower() for each in face_cards]
        # spot card is any non-face/non-ace but including ten
        self.top_spot = top_spot
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
            # start with ace if needed - indicated in self.face_cards
            if "ace" in self.face_cards:
                card = Card(each, 1, "ace")
                self.cards.append(card)
            # go thru cards 2-10
            for i in range(2, self.top_spot+1):
                # create card
                card = Card(each, i)
                # add card to list of cards
                self.cards.append(card)
            # create jack, queen, king if needed - check if face cards is not None
            if self.face_cards is not None:
                # loop thru each index in face_cards
                for i in range(len(self.face_cards)):
                    # skip if card is "ace"
                    if self.face_cards[i] == "ace":
                        pass
                    # assign other face card values
                    else:
                        card = Card(each,
                                    self.top_spot+1,
                                    self.face_cards[i])
                        self.cards.append(card)

    def deck_storage(self, cards):
        for i in range(len(cards)):
            # first card
            if i == 0:
                # make first card bottom of deck
                self.bottom = cards[i]
                cards.prev = None
                cards.next = cards[i+1]
    


class Card:
    def __init__(self, suit=None, value=None, name = None):
        self.suit = suit
        self.value = value
        # linked list elements
        self.next = None
        self.prev = None

        # optional name for assigning face card values or joker values
        self.card_name = name

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
