import random
import os
import time
from cs50 import get_int
from cs50 import get_string
import sys

#initialization of all variables
cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", ]
player_cards = []
dealer_cards = []
player_value = 0
dealer_value = 0
chips = 100
bet = 0

#function that restarts the deck after a round is played and starts a new game
def restart():
    global player_cards
    global dealer_cards
    global player_value
    global dealer_value
    global bet
    list.clear(player_cards)
    list.clear(dealer_cards)
    player_value = 0
    dealer_value = 0
    bet = 0
    deal()

#Function that deals and prints first cards
def deal():
    if (chips <= 0):
        print("You have no more chips :/")
        sys.exit(0)
    bet_chips()
    for i in range(2):
        player_cards.append(random.choice(cards))
    write_player()
    for j in range(2):
        dealer_cards.append(random.choice(cards))
    print("Dealer Card: " + dealer_cards[0])
    time.sleep(2)
    count_value()

#bet function
def bet_chips():
    global bet
    global chips
    bet = get_int("You have " + str(chips) + " chips. How many would you like to bet? ")
    if (bet > chips):
        print("INVALID BET")
        bet_chips()
    if (bet <= 0):
        print("INVALID BET")
        bet_chips()

#Function that writes all of the players cards
def write_player():
    for card in player_cards:
        print("Player Card: " + card)

#Function that writes the dealers cards
def write_dealer():
    for card in dealer_cards:
        print("Dealer card: " + card)
#function that counts and adds up value of player and dealer cards
def count_value():
    global player_value
    global dealer_value
    for card in player_cards:
        if (card == "Ace"):
            get_ace()
        elif (card == "Two"):
            player_value += 2
        elif (card == "Three"):
            player_value += 3
        elif (card == "Four"):
            player_value += 4
        elif (card == "Five"):
            player_value += 5
        elif (card == "Six"):
            player_value += 6
        elif (card == "Seven"):
            player_value += 7
        elif (card == "Eight"):
            player_value += 8
        elif (card == "Nine"):
            player_value += 9
        elif (card == "Ten"):
            player_value += 10
        elif (card == "Jack"):
            player_value += 10
        elif (card == "Queen"):
            player_value += 10
        elif (card == "King"):
            player_value += 10
    for card in dealer_cards:
        if (card == "Ace"):
            dealer_ace()
        elif (card == "Two"):
            dealer_value += 2
        elif (card == "Three"):
            dealer_value += 3
        elif (card == "Four"):
            dealer_value += 4
        elif (card == "Five"):
            dealer_value += 5
        elif (card == "Six"):
            dealer_value += 6
        elif (card == "Seven"):
            dealer_value += 7
        elif (card == "Eight"):
            dealer_value += 8
        elif (card == "Nine"):
            dealer_value += 9
        elif (card == "Ten"):
            dealer_value += 10
        elif (card == "Jack"):
            dealer_value += 10
        elif (card == "Queen"):
            dealer_value += 10
        elif (card == "King"):
            dealer_value += 10
    choice()

#updates card value
def update_player():
    global player_value
    card = player_cards[-1]
    if (card == "Ace"):
        get_ace()
    elif (card == "Two"):
        player_value += 2
    elif (card == "Three"):
        player_value += 3
    elif (card == "Four"):
        player_value += 4
    elif (card == "Five"):
        player_value += 5
    elif (card == "Six"):
        player_value += 6
    elif (card == "Seven"):
        player_value += 7
    elif (card == "Eight"):
        player_value += 8
    elif (card == "Nine"):
        player_value += 9
    elif (card == "Ten"):
        player_value += 10
    elif (card == "Jack"):
        player_value += 10
    elif (card == "Queen"):
        player_value += 10
    elif (card == "King"):
        player_value += 10

#updates dealer card value
def update_dealer():
    global dealer_value
    card = dealer_cards[-1]
    if (card == "Ace"):
        dealer_ace()
    elif (card == "Two"):
        dealer_value += 2
    elif (card == "Three"):
        dealer_value += 3
    elif (card == "Four"):
        dealer_value += 4
    elif (card == "Five"):
        dealer_value += 5
    elif (card == "Six"):
        dealer_value += 6
    elif (card == "Seven"):
        dealer_value += 7
    elif (card == "Eight"):
        dealer_value += 8
    elif (card == "Nine"):
        dealer_value += 9
    elif (card == "Ten"):
        dealer_value += 10
    elif (card == "Jack"):
        dealer_value += 10
    elif (card == "Queen"):
        dealer_value += 10
    elif (card == "King"):
        dealer_value += 10

#Function that manages player ace choice
def get_ace():
    global player_value
    if (player_value >= 11):
        player_value += 1
    else:
        card_value = get_int("Ace Value: ")
        if (card_value != 1 and card_value != 11):
            print("Invalid Ace Value")
            get_ace()
        else:
            player_value += card_value
    choice()

#function that manages dealer ace choice
def dealer_ace():
    global dealer_value
    if (dealer_value < 11):
        dealer_value += 11
    else:
        dealer_value += 1
    dealer_go()

#function that allows for a hit or stay
def choice():
    global chips
    global bet
    response = get_string("Hit or stay? ")
    if response.lower() != "hit" and response.lower() != "stay":
        choice()
    if response.lower() == "hit":
        os.system("clear")
        player_cards.append(random.choice(cards))
        write_player()
        update_player()
        if (player_value > 21):
            print("Bust!")
            chips -= bet
            time.sleep(5)
            restart()
        else:
            choice()
    if response.lower() == "stay":
        os.system("clear")
        dealer_go()

def dealer_go():
    global chips
    global bet
    global dealer_value
    write_dealer()
    while (dealer_value < 17):
        dealer_cards.append(random.choice(cards))
        update_dealer()
        os.system("clear")
        write_dealer()
        if (dealer_value > 21):
            print("Dealer Busted")
            chips += bet
            time.sleep(5)
            restart()
    compare_value()


def compare_value():
    global player_value
    global dealer_value
    global chips
    global bet
    write_player()
    if (player_value == dealer_value):
        print("Push")
        time.sleep(5)
        restart()
    elif(player_value > dealer_value):
        print("You Win!")
        chips += bet
        time.sleep(5)
        restart()
    else:
        print("Dealer wins")
        chips -= bet
        time.sleep(5)
        restart()




#starts the game
deal()




