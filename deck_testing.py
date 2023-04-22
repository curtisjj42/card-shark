import deck_builder as db
import unittest


class test_Card(unittest.TestCase):
    def test_blank_card(self):
        card = db.Card()
        self.assertEqual(card.get_data(), ('None', 'None'))

    def test_update_attributes(self):
        # create blank card
        card = db.Card()
        # update suit, value
        card.set_suit('spade')
        card.set_name('ace')

        self.assertEqual(card.get_data(), ('ace', 'spade'))

        # create a new card
        card2 = db.Card('hearts', '8')

        card.set_next(card2)
        card2.set_prev(card)

        # check all next and prev
        self.assertEqual(card.get_next(), card2)
        self.assertEqual(card2.get_prev(), card)
        self.assertEqual(card.get_prev(), None)
        self.assertEqual(card2.get_next(), None)

    def create_card(self):
        card = db.Card('hearts', 8)
        card2 = db.Card()

        self.assertEqual(card.get_data(), ('8', 'Hearts'))
        # test length
        self.assertEqual(len(card), 1)
        self.assertNotEqual(len(card), len(card2))

    def test_equality(self):
        card = db.Card('clubs', '3')
        card2 = db.Card()
        card2.set_name(3)
        card2.set_suit('CLUBS')

        self.assertEqual(card, card2)


class test_Deck(unittest.TestCase):

    def test_build_deck(self):

        # create a deck
        deck = db.Deck()
        self.assertIsInstance(deck, db.Deck)

        # create a deck with jokers
        deck = db.Deck(jokers=True)
        self.assertIsInstance(deck, db.Deck)
        # check that jokers are in the deck
        deck.find('bjoker')
        deck.find('rjoker')

    def test_equal(self):

        # create a deck
        deck = db.Deck()
        # full deck length test
        self.assertEqual(len(deck), 52)
        # pull a card and test length
        deck.pull('h2')
        self.assertEqual(len(deck), 51)

        # test that iterating through deck yields each card
        deck = db.Deck()
        n = 0
        for _ in deck:
            n += 1
        self.assertEqual(len(deck), n)

        # create two identical decks to check against
        deck2 = db.Deck()
        self.assertEqual(deck, deck2)

        # create two decks, add a card to the second deck that exists
        deck1 = db.Deck()
        deck2 = db.Deck()
        deck2.push('hearts', 2)
        self.assertNotEqual(deck1, deck2)

    def test_shuffle(self):
        """
        There is a miniscule chance that the shuffled decks equal each other
        This is a consequence of true randomness, and is considered small enough to ignore
        If it proves to be an error, run test again
        """

        # create two decks to compare
        deck1 = db.Deck()
        deck2 = db.Deck()

        # shuffle deck three times
        self.assertNotEqual(deck1, deck2.shuffle())
        self.assertNotEqual(deck1, deck2.shuffle())
        self.assertNotEqual(deck1, deck2.shuffle())
        # remake deck 2 and shuffle both decks to see if first shuffle is not equal
        deck2 = db.Deck()
        deck1.shuffle()
        deck2.shuffle()
        self.assertNotEqual(deck1, deck2)

    def test_find(self):

        deck = db.Deck()

        # try to find a known card at top of deck
        i = deck.find('h2')
        self.assertEqual(i, 0)

        # try to find a card known to not be in the deck
        msg = deck.find('h22')
        self.assertEqual(msg, "Target card is not in this deck")

        # try to use a list on find - use deck.pull_list!
        msg = deck.find(['h2', 'h3'])
        self.assertEqual(msg, "Target card is not in this deck")

    def test_pull(self):

        # create deck for testing
        deck = db.Deck()

        # pull top card
        top = deck.top
        top = top.__str__()
        deck.pull(top)
        # check that top card is no longer in deck
        for each in deck:
            card = db.Card(each[1], each[0]).__str__()
            self.assertNotEqual(card, top)

        # pull bottom card
        bottom = deck.bottom
        bottom = bottom.__str__()
        deck.pull(bottom)
        # check that bottom card is no longer in deck
        for each in deck:
            card = db.Card(each[1], each[0]).__str__()
            self.assertNotEqual(card, bottom)

        # pull any other card
        card = db.Card('hearts', 8)
        deck.pull(card.__str__())

        # pull a card that doesn't exist
        card = db.Card('suit', 11)
        card_pull = card.__str__()
        self.assertEqual(deck.pull(card_pull), "Target card is not in this deck")

        # pull a card again after trying to pull once
        pulled_card = deck.pull('hace')
        # pulled successfully
        self.assertEqual(pulled_card, db.Card('hearts', 'ace').get_data())
        # try to pull again
        self.assertEqual(deck.pull('hace'), "Target card is not in this deck")

        # try to pull with blank input
        with self.assertRaises(TypeError):
            deck.pull()

    def test_pull_list(self):

        deck = db.Deck()

        pull_list = ['h'] * 13
        cards = []
        for each in range(2, 11):
            cards.append(each)
        for each in ['jack', 'queen', 'king', 'ace']:
            cards.append(each)

        for i in range(len(pull_list)):
            pull_list[i] = pull_list[i] + str(cards[i])

        # store top card for later
        old_top = deck.top

        # pull all hearts
        deck.pull_list(pull_list)

        # try to find a heart card or two
        self.assertEqual(deck.find('h3'), "Target card is not in this deck")
        self.assertEqual(deck.find('hking'), "Target card is not in this deck")
        self.assertEqual(deck.pull('h8'), "Target card is not in this deck")
        # check that length is 13 fewer
        self.assertEqual(len(deck), 39)

        # check that top card changed
        self.assertNotEqual(deck.top, old_top)

    def test_cut(self):

        # create two decks to compare
        deck1 = db.Deck()
        deck2 = db.Deck()

        # cut deck2 and compare to original deck
        deck2.cut()
        self.assertNotEqual(deck1, deck2)

        # cut other deck again to compare consistency
        deck1.cut()
        self.assertEqual(deck1, deck2)

        # cut deck 2 once more and compare
        deck2.cut()
        self.assertNotEqual(deck1, deck2)

        # cut deck, make sure top and bottom updated
        deck = db.Deck()
        old_top = deck.top
        old_bottom = deck.bottom
        deck.cut()
        self.assertNotEqual(deck.top, old_top)
        self.assertNotEqual(deck.bottom, old_bottom)
        self.assertEqual(deck.top.get_prev(), None)
        self.assertEqual(deck.bottom.get_next(), None)

    def test_deal(self):
        pass
        # UPDATE WHEN DEAL IS READY

    def test_push_card(self):

        # create a new deck
        deck = db.Deck()

        # push a new card, a joker
        deck.push('black', 'joker')
        i = deck.find('bjoker')
        # check that card was pushed to top of deck
        self.assertEqual(i, len(deck) - 1)
        # check that length updated
        self.assertEqual(len(deck), 53)

        # try to push a card that already exists (should pass)
        deck.push('hearts', 2)
        self.assertEqual(len(deck), 54)
        # now, you can pull it twice
        deck.pull('h2')
        deck.pull('h2')
        self.assertEqual(len(deck), 52)  # length with one joker!

        # try to push nothing
        with self.assertRaises(TypeError):
            deck.push()

        # can even push a none card to the deck
        deck.push(None, None)

    def test_push_deck(self):
        """Try to push a deck into another deck"""

        deck1 = db.Deck()
        deck2 = db.Deck()
        # loop through push
        for each in deck2:
            deck1.push(each[1], each[0])
        # check that it's the length of two decks
        self.assertEqual(len(deck1), 104)


