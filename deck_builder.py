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

        index = self.find(pull) #finds index of the card you want to pull
        if index == 0:
            # If we pull / del the card at index 0
            self.cards[index + 1].set_prev(len(self.cards)) # sets the card after to have .prev = last card in list
            self.cards[len(self.cards) - 1].set_next(self.cards[index + 1]) # sets the card before to have .next = next card
            self.cards.remove(self.cards[index]) # removes card

        elif index == (len(self.cards) - 1):
            # If we pull/ del the last card in the list
            self.cards[0].set_prev(self.cards[index - 1]) # sets card[0] to .prev = last in list
            self.cards[index - 1].set_next(self.cards[0]) # sets new last card to .next = first in list
            self.cards.remove(self.cards[index]) # removes card

        else:
            # if we pull / del any card that is not in position 0 or in the last position in the list
            self.cards[index + 1].set_prev(self.cards[index - 1]) # sets .prev
            self.cards[index - 1].set_next(self.cards[index + 1]) # sets .next
            self.cards.remove(self.cards[index]) # removes card

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
        cut_deck = [] #temporary list to store new order
        for i in range(cut_index, len(self.cards)): # for each item from the cut down, 
            cut_deck.append(self.cards[i]) #append it to the front of the new list
        for i in range(0, cut_index): # for each item from the cut up (what you move to the botton of the deck), 
            cut_deck.append(self.cards[i]) # add it to the new list
        self.cards = cut_deck

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
