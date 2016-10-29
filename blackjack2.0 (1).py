# Nathaniel Betts
# 10/24/2016
# Week 9 Assignment
# Blackjack
# Creates multiple decks depending on how many decks user wants
# shuffles cards and places into shoe
# draws card from shoe and deals to player
# calculates value of cards
# displays busts or wins
# allows user to stand
# adds totals of wins, busts and stands
# displays scores at end of game

# import
import random

# constants
# =====================================================================================================================
CLUB = "\u2663"
HEART = "\u2665"
DIAMOND = "\u2666"
SPADE = "\u2660"

SUITS = (CLUB, HEART, DIAMOND, SPADE)
PIPS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

# Functions
# =====================================================================================================================

# Creates deck
def create_deck():
    full_deck = []
    for suit in SUITS:
        for pip in PIPS:
            entry = (suit, pip)
            full_deck.append(entry)
    return full_deck

# used to pull random card from deck and place into shoe
# based on how many decks user chooses to use
def shuffle():
    max_range = len(deck)
    index = random.randrange(max_range)
    card = deck[index]
    del deck[index]
    return card

# input verification for shoe
def shoe_ver(shoe):
    while shoe not in range(1, 7):
        while not shoe:
            print("Please enter a number(1-6): ")
            shoe = input("")
        try:
            shoe = int(shoe)
            if shoe > 6:
                print("casino shoe can only hold 6")
                shoe = input("Please enter a number(1-6)")
        except ValueError:
            print("invalid entry")
            shoe = input("Please enter a number(1-6)")
    return shoe

# Draw's card from shoe
def draw_card():
    card = shoe[0]
    del shoe[0]
    return card

# Finds vale of players hand
# pulls ace out to calculate ace after all other cards
# have been calculated
def sum_hand(hand):
    hand_val = 0
    holding = []
    for card in hand:
        suit, pip = card
        if pip == "A":
            holding += "A"
        elif pip == "10" or pip == "J" or pip == "Q" or pip == "K":
            hand_val += 10
        else:
            hand_val += int(pip)
    for card in holding:
        if card == "A":
            if hand_val <= 10:
                hand_val += 11
            else:
                hand_val += 1
    return hand_val


# unpacks tuples in hand and prints card in more appealing way
def print_hand(hand):
    for tup in hand:
        suit, pip = tup
        card = suit + pip
        print(card, end=" ")
    print()

# Play again
def play_again(userin):
    play = 0
    userin = userin.lower()
    while not userin:
        input("please enter a y or n")
    while userin != "y" and userin != "n":
        print("y or n")
        userin = input("")
    if userin == "n":
        play += 1
    elif userin == "y":
        play = 0
    return play

def shoe_len(shoe):
    max_len = len(shoe)
    if max_len <= 10:
        new_shoe = 1
    else:
        new_shoe = 0
    return new_shoe


# Program
# =====================================================================================================================

# Shoe creation
# uses create_deck function with shuffle and shoe_ver to create the shoe for game
wins = 0
busts = 0
stand = 0
play = 0
shoe = []
while not play:
    new_shoe = shoe_len(shoe)
    while new_shoe == 1:
        num_shoes = shoe_ver(input("How many Decks would you like in your shoe?"))
        while num_shoes != 0:
            deck = create_deck()
            for i in range(52):
                shoe.append(shuffle())
            num_shoes -= 1
        new_shoe -= 1
    #player hand:
    input("press enter for your hand")
    print("\n" * 30)
    hand = []
    hand.append(draw_card())
    hand.append(draw_card())
    print_hand(hand)
    sum_hand(hand)
    if sum_hand(hand) == 21:
        print("Congratulations you have a natural hand!")
        wins += 1
        play = play_again("Would you like to play again?")
    else:
        while sum_hand(hand) <= 21:
            h_s = input("would you like to hit or stay?(h/s)")
            while not h_s:
                print("\n" * 30)
                h_s = input("Please enter a h or s")
            if sum_hand(hand) == 21:
                print("\n" * 30)
                print("Congratulations you won")
                wins += 1
                play = play_again(input("Would you like to play again?(y/n"))
                break
            elif h_s == "h":
                print("\n" * 30)
                hand.append(draw_card())
                sum_hand(hand)
                print_hand(hand)
            elif h_s == "s":
                print("\n" * 30)
                print_hand(hand)
                print("you have chosen to stand")
                stand += 1
                play = play_again(input("would you like to play again?(y/n"))
                break
        else:
            print("\n" * 30)
            print_hand(hand)
            print("You have busted")
            busts += 1
            play = play_again(input("Would you like to play again?(y/n)"))

else:
    print("\n" * 30)
    print("You have won ", wins, " times.")
    print("You have busted ", busts, " times.")
    print("You have stood ", stand, " times.")
    print("Thanks for playing!!")
    print("Press enter to exit")
    input("")

