# Nathaniel Betts
# 10/17/2016
# Week 9 Assignment
# Blackjack
# creates deck of cards
# draws random card from deck
# deletes card drawn from deck
# prints cards drawn in 4 x 13 grid

# import
import random

# constants
CLUB = "\u2663"
HEART = "\u2665"
DIAMOND = "\u2666"
SPADE = "\u2660"

SUITS = (CLUB, HEART, DIAMOND, SPADE)
PIPS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

# Functions

# Creates deck
def create_deck():
    full_deck = []
    for suit in SUITS:
        for pip in PIPS:
            entry = (pip, suit)
            full_deck.append(entry)
    return full_deck

# Draws card from deck
def draw_card():
    max_range = len(deck)
    index = random.randrange(max_range)
    suit, pip = deck[index]
    card = suit + pip
    del deck[index]
    return card

shoe = int(input("How many decks would you like(1-3)"))
while shoe != 0:
    if shoe in range(1, 4):
        deck = create_deck()
        # prints deck in 4 x 13 grid
        for i in range(13):
            for j in range(4):
                print(draw_card(), end=" ")
            print()
        print()
        shoe -= 1
    else:
        print("Casino rules only allow 3")
        shoe = int(input("How many decks would you like?"))
input("Press any key to exit")
