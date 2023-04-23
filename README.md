# Card-Shark: Deck Constructor
Card-Shark is a simple deck constructor made in Python 3.1
##### Project Status: Last Updated April 2023
# Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Examples](#examples)
- [Testing](#testing)
- [Sources](#sources)
- [Team](#team)

## Overview
Card-Shark is a simple deck constructor Python package that allows developers to easily create and manage decks and cards without having to worry about basic functions. This package will allow you to focus on implmenting game-specific rules and mechanics.

Card-Shark was created as a final project for [Introduction to Programming for Data Science](https://kuwisdelu.github.io/ds5010-spring23.html) course at Northeastern taught by Kylie Bemis. Throughout creating this package we learned to implement class concepts such as linked lists, testing, github and overall coding collaboration. 


## Features
- Create a new deck
- Shuffle
- Deal
- Cut
- Pull / Draw
- Find a card
- Push add a card

## Technologies
- Python 3.1

## Setup


## Examples
```python
import card-shark

# create a deck
deck = Deck()

# print the top card
print(f"Top card is: {deck.top}")

# pull top card
pulled_card = deck.pull('h2')
print(f"Top card is: {deck.top}")
print(f"Pulled card is: {pulled_card}")

# pull two cards at once
deck.pull_list(['h8', 'sace'])

# try to find the ace of spades now
print("Trying to find ace of spades after pulling it from deck:")
print(deck.find('sace'))

# shuffle deck
print(f"Unshuffled deck: {deck}")
deck.shuffle()
print(f"Shuffled deck: {deck}")

# create two decks
deck1 = Deck()
deck2 = Deck()

# push each card in deck2 into deck1 with loop
for each in deck2:
    deck1.push(each[1], each[0])

# print new deck1
print(deck1)
print(f"Length of deck1 is: {len(deck1)}")
```


## Testing
Unit testing is performed in the deck_testing.py file. This file runs tests on both the Card and Deck classes, including most methods. 

Some notable considerations when performing unit testing:
- Card: Card objects should be constructed with only a string or None type suit, and any name input. Card objects can only be linked (previous or next) to another instance of a Card object, or to None. 
- Deck: Deck.push(), Deck.pull(). Deck.pull_list(), and Deck.find() all take a string representation of a card as input. A Card object cannot be directly passed into these methods. If a card has a suit of hearts and value of 8, then you must pass 'h8' into these methods to interacte with this card. Additionally, you cannot pass a tuple representing the card data into these methods, such as ('8', 'hearts') for the previous example. 
- Testing shuffle by comparing it against a default deck is a good way to test if the deck was shuffled, and this can be done multiple times. However, there is an extremely minute chance that shuffling a deck with result in the same order as the original deck. This is an issue with the inherent value of true randomness used in the shuffle. 

## Sources
Only two external packages were used in this package: 
- [Random][rand]. Used to facilitate a truly random shuffle of the deck.
- [Unittest][unit]. Used in deck_testing.py unit testing module.


[rand]: https://github.com/python/cpython/blob/3.11/Lib/random.py
[unit]: https://docs.python.org/3/library/unittest.html#module-unittest

## Team
- Jason Curtis | [Github](https://github.com/curtisjj42)
- Alex Kramer | [Github](https://github.com/Alex-Kramer0)
- Zack Armand | [Github](https://github.com/ZacharyArmandNEU)
