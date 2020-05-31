''' Plays a game of Bridge with 3 Bots and 1 Human '''
import os
import time
import constants as c
from random import randint
from card import Card
from deck import Deck
from bot import BridgeBot
from human import BridgeHuman


############
# FUNCTIONS
############

def clear_screen():
    '''
    Function to clear user's screen after each round.
    'nt' for windows, 'posix' for mac and linux
    '''
    _ = os.system('cls') if os.name == 'nt' else os.system('clear')


def update_seen_card(player, card):
    ''' Run see_card() for all Bots. '''
    for p in PLAYERS:
        # for Bots
        try:
            p.see_card(player, card)
        # for Humans
        except:
            pass


def play_round(starter_num):
    '''
    starter_num: number of first player to place a card for this round

    Play one round in bridge, where all 4 players place a card each.

    Returns player number of this round's winner.
    '''
    global ROUNDS_PLAYED
    
    if starter_num not in range(4):
        raise ValueError(c.red(c.PLAYER_NUMBER_ERR))

    pile = {}

    # starter (either Human / Bot) plays a card
    start_card = PLAYERS[starter_num].play_card(None)

    # start_card is added to pile
    pile[starter_num] = start_card

    # let Bots see card
    update_seen_card(starter_num, start_card)

    # go through next three players who need to play the same suit
    for num in range(starter_num+1, starter_num+4):
        # restart from 0 if player number > 3
        num %= 4

        if isinstance(PLAYERS[num], BridgeBot):
        	time.sleep(1)

        # same process as above
        card = PLAYERS[num].play_card(round_suit=start_card.suit)
        pile[num] = card
        update_seen_card(num, card)

    winner = max(
        pile,
        key=lambda x: pile[x].get_bridge_strength(start_card.suit)
    )

    PLAYERS[winner].score += 1

    ROUNDS_PLAYED += 1

    return winner


#############
# START GAME
#############

# counter for number of rounds played
ROUNDS_PLAYED = 0

# get a list of 4 hands of cards
HANDS = Deck().deal(n=c.NUM_PLAYERS, shuffle_deck=True)

# list to hold Players
PLAYERS = []

# user input for name
clear_screen()
name = input('Enter your name:\n')

# set 1 human player as num = 0 and name as user input name
for i in range(len(HANDS)):
    if i == 0:
        PLAYERS.append(BridgeHuman(HANDS[i], i, name))
    else:
        PLAYERS.append(BridgeBot(HANDS[i], i))

# randomly choose a player number to start.
STARTER = randint(0, 3)

while ROUNDS_PLAYED < c.TOTAL_ROUNDS:
    clear_screen()

    # print instructions
    print(f'Hi {name},')
    print(c.INSTRUCTIONS)

    print(f'\nTRUMP SUIT: {c.SUITS[c.TRUMP_SUIT]}\n')

    print('----------')
    print(f' Round {ROUNDS_PLAYED} ')
    print('----------')

    # winner starts each round from round 1 onwards.
    STARTER = play_round(STARTER)

    print(f'\n> Round {ROUNDS_PLAYED} Winner: {c.green(PLAYERS[STARTER].name)}\n')

    # if final round, print header for final score
    if ROUNDS_PLAYED == c.TOTAL_ROUNDS:
        print(c.green(c.FINAL_SCORE_HEADER))

    for p in PLAYERS:
        print(c.green(f"{p.name}'s score: {p.score} sets"))

    _ = input('\n\nPress Enter to continue.')