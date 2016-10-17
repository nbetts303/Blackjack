# Nathaniel Betts
# 10/17/2016
# Week 9 Assignment
# Blackjack

# import
import random

# constants
CLUB = "\u2663"
HEART = "\u2665"
DIAMOND = "\u2666"
SPADE = "\u2660"

SPADEWT = "\u2664"
HEARTWT = "\u2661"
DIAMONDWT = "\u2662"
CLUBWT = "\u2667"
SUITS = (CLUB, CLUBWT, HEART, HEARTWT, DIAMOND, DIAMONDWT, SPADE, SPADEWT)
PIPS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

# list
deck = []
max_range = len(deck)
index = range(int(max_range))

for suit in SUITS:
    for pip in PIPS:
        deck += (suit, pip)
print(deck)

def deal_card():
    for cards in deck:
        print(cards[index])
        del deck[cards]

print(deal_card())