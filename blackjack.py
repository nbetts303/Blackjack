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

def create_deck():
    full_deck = []
    for suit in SUITS:
        for pip in PIPS:
            entry = (pip, suit)
            full_deck.append(entry)
    return full_deck

print(create_deck())
print()