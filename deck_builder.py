import random


class Deck:
    def __init__(self, jokers=False):
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

    def __str__(self):
        """Returns list with string representation of each card in deck"""
        # list comprehension using string value of each card in card container
        return str([each.__str__() for each in self.cards])

    def __len__(self):
        """Return length of internal list of cards"""
        return len(self.cards)

    def __iter__(self):
        """Returns iterable consisting of self-contained list of cards"""
        return iter(self.cards)

    def build_deck(self):
        """
        Constructs standard deck of cards with 52 cards and four suits
        :return: None.
        """
        # go through each suit
        for each in self.suits:
            # go through cards 2-top spot (standard case is 10)
            for i in range(2, 11):
                # create card
                card = Card(each, i)
                # add card to list of cards
                self.cards.append(card)
            # create jack, queen, king if needed - check if face cards is not None
            for face in self.face_cards:
                card = Card(each, face)
                self.cards.append(card)
        # link cards in deck together
        self.deck_storage()

    def deck_storage(self):
        """
        Iterates through internal cardholder list, linked each card sequentially
        :return: None
        """

        # loop through each card in deck
        for i in range(len(self.cards)):
            # first card
            if i == 0:
                # make first card bottom of deck
                self.bottom = self.cards[i]
                self.cards[i].prev = None
                self.cards[i].next = self.cards[i + 1]
            # last card
            elif i == len(self.cards) - 1:
                # make last card top of deck
                self.top = self.cards[i]
                self.cards[i].prev = self.cards[i - 1]
                self.cards[i].next = None
            # rest of the cards
            else:
                self.cards[i].prev = self.cards[i - 1]
                self.cards[i].next = self.cards[i + 1]

    def find(self, card):
        '''
        Finds a specific card in the deck, returns its location (index)
        :parameter card: card you are finding
        :return: location as an index
        '''
        index = 0
        for item in self.cards:
            if str(item) == card:
                return index
            index += 1

    def pull(self, pull):
        '''
        Removes one card from the deck at a time,
        :param pull: card that is to be pulled out of the deck, removed
        :return:No returns, mutates self.cards list and individual card's pointers within Card class

        Example for team to understand logic:
            {0} -> {1} -> {2} -> {3}
            if we remove {0}, we set: {1}.prev = {3} or index -1; {3}.next = {1} or index +1
            if we remove {3}, we set: {0}.prev = {2} or index -1; {2}.next = {0} or 0
            if we remove {1}, we set: {2}.prev = {0} or index -1; {0}.next = {2} or index +1
        '''

        index = self.find(pull)  # finds index of the card you want to pull
        if index == 0:
            # If we pull / del the card at index 0
            self.cards[index + 1].set_prev(len(self.cards))  # sets the card after to have .prev = last card in list
            self.cards[len(self.cards) - 1].set_next(
                self.cards[index + 1])  # sets the card before to have .next = next card
            self.cards.remove(self.cards[index])  # removes card

        elif index == (len(self.cards) - 1):
            # If we pull/ del the last card in the list
            self.cards[0].set_prev(self.cards[index - 1])  # sets card[0] to .prev = last in list
            self.cards[index - 1].set_next(self.cards[0])  # sets new last card to .next = first in list
            self.cards.remove(self.cards[index])  # removes card

        else:
            # if we pull / del any card that is not in position 0 or in the last position in the list
            self.cards[index + 1].set_prev(self.cards[index - 1])  # sets .prev
            self.cards[index - 1].set_next(self.cards[index + 1])  # sets .next
            self.cards.remove(self.cards[index])  # removes card

    def pull_list(self, cards=list):
        '''
        Pulls / removes a list of cards from the deck
        :parameter cards: a list of strings
        :return: mutates list
        '''
        for card in cards:
            self.pull(card.lower())

    def cut(self):
        '''
        Cuts deck in half, and
        :return: updates the currect deck
        '''
        cut_index = len(self.cards) // 2
        # where the cut is taking place
        cut_deck = []  # temporary list to store new order
        for i in range(cut_index, len(self.cards)):  # for each item from the cut down,
            cut_deck.append(self.cards[i])  # append it to the front of the new list
        for i in range(0, cut_index):  # for each item from the cut up (what you move to the botton of the deck),
            cut_deck.append(self.cards[i])  # add it to the new list
        self.cards = cut_deck

    def deal(self, deal_from="Top", n_cards=1):
        """
        Deals a deck of cards of n_cards length to user
        :param deal_from: where to deal cards from in deck
            Options include top, bottom, middle, random
            Defaults to dealing from top of deck
        :param n_cards: number of cards to deal. Defaults to one card
        :return: a hand of cards (list) of length n_cards
        """

        # lowercase deal_from string for input consistency
        deal_from = deal_from.lower()
        # get length of deck from self.cards
        n = len(self.cards)

        # check if card number input is valid
        if n_cards > len(self.cards):
            return "Error: number of cards entered larger than deck"
        # return empty hand if n_cards is 0, error if less than 0
        elif n_cards == 0:
            return []
        elif n_cards < 0:
            return "Error: number of cards entered less than 0"

        # match deal_from input to output
        match deal_from:
            case "top":
                deal = []
                # iterate through list starting from top
                for i in range(1, n_cards + 1):
                    dealt_card = self.cards.pop(n - i)
                    # remove prev, next attributes as card outside of deck
                    dealt_card.next, dealt_card.prev = None, None
                    # add card to dealt hand
                    deal.append(dealt_card)
                # reassign top card
                if n_cards == n:
                    self.top, self.bottom = None, None
                else:
                    self.top = self.cards[n - n_cards - 1]
                    self.top.set_next(None)
                return deal
            case "bottom":
                deal = []
                for i in range(n_cards):
                    # remove card from bottom of deck
                    dealt_card = self.cards.pop(0)
                    # remove prev, next attributes as card outside of deck
                    dealt_card.next, dealt_card.prev = None, None
                    # add card to dealt hand
                    deal.append(dealt_card)
                # reassign bottom card
                if n_cards == n:
                    self.top, self.bottom = None, None
                else:
                    self.bottom = self.cards[0]
                    self.bottom.set_prev(None)
                return deal
            case "middle":
                # empty list to hold deal
                deal = []
                for i in range(n_cards):
                    mid = n // 2
                    # remove card from middle of deck
                    dealt_card = self.cards.pop(mid)
                    # remove prev, next attributes as card outside of deck
                    dealt_card.next, dealt_card.prev = None, None
                    # add card to dealt hand
                    deal.append(dealt_card)
                    # reduce stored length of deck
                    n -= 1
                # reassign top, bottom, internal structure as needed
                if n == 0:
                    self.top, self.bottom = None, None
                elif n == 1:
                    self.bottom, self.top = self.cards[0], self.cards[0]
                    self.bottom.set_prev(None)
                    self.bottom.set_next(None)
                else:
                    self.deck_storage()
                return deal
            case "random":
                # if dealing size of deck, return deck, but shuffled
                if n_cards == n:
                    deal = self.cards.copy()
                    random.shuffle(deal)
                    return deal
                deal = []
                i = 0
                # iterate through number of cards to deal
                while i < n_cards:
                    # choose random number between 1 and length of deck
                    m = random.randrange(1, n)
                    dealt_card = self.cards.pop(m)
                    # remove prev, next attributes as card outside of deck
                    dealt_card.next, dealt_card.prev = None, None
                    # add card to dealt hand
                    deal.append(dealt_card)
                    # update iterators
                    i += 1
                    n -= 1
                # reassign cards and list structure
                if n == 1:
                    self.top, self.bottom = self.cards[0], self.cards[0]
                    self.bottom.set_prev(None)
                    self.bottom.set_next(None)
                else:
                    self.deck_storage()
                return deal
            # any other deal_from option results in error
            case _:
                return "Error: deal_from input invalid"


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

    def __eq__(self, other):
        """Compares the suit/value of two cards"""
        if self.name == other.value and self.suit == other.suit:
            return True
        return False

    def __len__(self):
        """A single instance of a card with always be of length one"""
        return 1

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
