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
        # initialize deck size counter
        self.size = 0
        # list to hold all cards
        self.cards = []
        # create deck
        self.build_deck()

    def __str__(self):
        """Returns list with string representation of each card in deck"""
        # list comprehension using string value of each card in card container
        return " -> ".join([str(x) for x in self])

    def __len__(self):
        """Return length of deck"""
        return self.size

    def __iter__(self):
        """Returns n-tuples containing name and suit of each card in deck of length n"""
        card = self.top
        while card is not None:
            yield card.get_data()
            card = card.get_next()

    def __eq__(self, other):
        """Two decks are equal if they contain the same exact cards in the same order"""
        if type(other) is Deck and len(self) == len(other):
            for each, other_each in zip(self, other):
                # catch any instance of cards not equaling in order
                if each != other_each:
                    return False
            # if all cards match, then decks equal
            return True
        # if other is not Deck class or length if different from self
        return False

    def build_deck(self):
        """
        Constructs standard deck of cards with 52 cards and four suits
        :return: None
        """

        for each in self.suits:
            # top card is the 2 of hearts
            for i in range(2, 11):
                self.push(each, f"{i}")
            for face in self.face_cards:
                self.push(each, face)
        # constructs two jokers if requested
        if self.jokers is True:
            self.push('red', 'joker')
            self.push('black', 'joker')

    def shuffle(self):
        """
        Shuffles cards to create a random distribution for game use
        :return: None, reorganization is handled within the card objects
        """

        i = 0
        # randomize the order of indices in initial constructor array
        assignments = []
        while i < self.size:
            rand = random.randint(0, self.size - 1)
            if rand not in assignments:
                assignments.append(rand)
                i += 1
        shuffled_order = [0 for _ in range(len(assignments))]
        card = self.top
        i = 0
        while card is not None:
            shuffled_order[assignments[i]] = card
            card = card.get_next()
            i += 1
        for j in range(len(shuffled_order)):
            if j == 0:
                self.top = shuffled_order[0]
                shuffled_order[0].set_prev(None)
                shuffled_order[0].set_next(shuffled_order[1])
            elif j == len(shuffled_order) - 1:
                self.bottom = shuffled_order[j]
                shuffled_order[j].set_next(None)
                shuffled_order[j].set_prev(shuffled_order[j-1])
            else:
                shuffled_order[j].set_prev(shuffled_order[j-1])
                shuffled_order[j].set_next(shuffled_order[j+1])

    def find(self, target):
        """
        Finds a specific card in the deck, returns location of first instance (index)
        :parameter target: card you are finding
        :return: location as an index of first instance of card in deck
        """

        index = 0
        # index acts as our counter for where we are
        card = self.top
        while card is not None:
            if card.__str__() == target:
                return index
            card = card.next
            index += 1
        return "Target card is not in this deck"

    def pull(self, target):
        """
        Removes one card from the deck at a time,
        :param target: card (ex. 'h2') that is to be pulled out of the deck, removed
        :return: No returns, mutates deck in place
        """

        card = self.top  # initialize with top card for iteration
        # iterate through the deck to reach the desired card
        while target != card.__str__():
            try:
                card = card.get_next()
            except AttributeError:
                # card not found, return error message
                return "Target card is not in this deck"

        if card == self.top:  # case 1: target is the top card
            data = card.get_data()  # preserve data during object deletion
            new_top = card.get_next()  # reset top card to next object
            new_top.set_prev(None)
            card = None  # delete pulled object
            self.size -= 1  # deck size reflects removed card
            self.top = new_top
            return data
        elif card == self.bottom:  # case 2: target is the bottom card
            data = card.get_data()
            new_bottom = card.get_prev()  # reset bottom card to previous object
            new_bottom.set_next(None)
            card = None
            self.size -= 1
            self.bottom = new_bottom
            return data
        else:                   # case 3: target is anywhere else in the deck
            data = card.get_data()
            new_prev = card.get_prev()  # link surrounding cards to each other
            new_next = card.get_next()
            new_prev.set_next(new_next)
            new_next.set_prev(new_prev)
            card = None
            self.size -=1
            return data

    def pull_list(self, cards: list):
        """
        Pulls / removes a list of cards from the deck
        :parameter cards: a list of strings
        :return: mutates list
        """
        for card in cards:
            self.pull(card.lower())

    def cut(self):
        """
        Cuts deck in half, and
        :return: updates the correct deck
        """
        cut_index = self.size // 2  # where the cut is taking place
        i = 0
        new_top = self.top  # loop to locate new deck top
        while i < cut_index:
            new_top = new_top.get_next()
            i += 1
        # bottom of the deck is the previous card
        new_bottom = new_top.get_prev()
        # top and bottom cards are now in the middle and linked
        self.bottom.set_next(self.top)
        self.top.set_prev(self.bottom)
        # set new top and bottom cards
        self.top = new_top
        new_top.set_prev(None)
        self.bottom = new_bottom
        new_bottom.set_next(None)

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
            raise Exception("Error: number of cards entered larger than deck")
        # return empty hand if n_cards is 0, error if less than 0
        elif n_cards == 0:
            return []
        elif n_cards < 0:
            raise Exception("Error: number of cards entered less than 0")

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
                raise Exception("Error: deal_from input invalid")

    def push(self, suit: str, name: str):
        """
        Creates and appends a new card into the deck, can be used as a method to
        'add' a card back into the deck
        :param suit: string of the suit
        :param name: strung of the name
        :return: no return, modifies the deck (linked list)
        """
        new_card = Card(suit, str(name))
        if self.bottom is None:
            self.top = new_card
            self.bottom = new_card
        else:
            new_card.prev = self.bottom
            self.bottom.next = new_card
            self.bottom = new_card
        self.size += 1
        # create the card object
        # appends the new card to the list


class Card:
    def __init__(self, suit=None, name=None):
        self.suit = str(suit)
        self.name = str(name)
        # linked list elements - default to no links (next, prev = None)
        self.next, self.prev = None, None

    def __str__(self):
        """Returns first letter of suit and value"""

        # if either suit or name is None, return None string
        if self.suit is None or self.name is None:
            return str(None)
        return str(self.suit[0]) + str(self.name)

    def __eq__(self, other):
        """
        Compares the suit/value of two cards objects, returning True if both match
        Comparison is case-independent
        """

        if self.name.lower() == other.name.lower() and self.suit.lower() == other.suit.lower():
            return True
        return False

    def __len__(self):
        """A single instance of a card with always be of length one"""
        return 1

    def set_prev(self, other):
        """Sets previous card value for linked list. Raises error if input is not Card or None"""
        if type(other) is not Card and other is not None:
            raise TypeError("Error: attempted to link an object that is not of class Card")
        self.prev = other

    def get_prev(self):
        """Getter method for previous card object in linked list"""
        return self.prev

    def set_next(self, other):
        """Sets next card value for linked list. Raises error if input is not Card or None"""
        if type(other) is not Card and other is not None:
            raise TypeError("Error: attempted to link an object that is not of class Card")
        self.next = other

    def get_next(self):
        """Getter method for next card object in linked list"""
        return self.next

    def set_suit(self, suit):
        """Method for setting card suit - converts input to string"""
        self.suit = str(suit)

    def set_name(self, name):
        """Method for setting card name - converts input to string"""
        self.name = str(name)

    def get_data(self):
        """Returns card data as a tuple"""
        return self.name, self.suit

