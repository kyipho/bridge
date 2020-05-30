from random import choice
from colorama import Fore, Style

# '2' to 'ace' strengths range from 1 to 13
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
RANK_STRENGTHS = {name: strength for strength, name in enumerate(RANKS, 1)}

# 'clubs' to 'spades' strengths range from 1 to 4
# use c/d/h/s to create cards, but print clubs/diamonds/hearts/spades symbols
SUITS = {'C': '♣', 'D': '♦', 'H': '♥', 'S': '♠'}
SUIT_STRENGTHS = {name: strength for strength, name in enumerate(SUITS, 1)}

# 4-player game
NUM_PLAYERS = 4

# 13 rounds in a bridge game
TOTAL_ROUNDS = 13

# whether at least 1 trump card has been played
# if True, player can start a round with a trump suit card
TRUMP_STARTED = False

# randomly pick a trump suit each game
TRUMP_SUIT = choice(list(SUITS))

# general error messages
RANK_ERR = f'\nRank must be in {RANKS}.\n'

SUIT_ERR = f'\nSuit must be in {list(SUITS)}.\n'

PLAYER_NUMBER_ERR = '\nPlayer number must be from 0-3.\n'

CARD_CLASS_ERR = '\nCard must be of Card class.\n'

DECK_INPUT_ERR = '\nInput to Deck must be a list of Cards.\n'

DEALT_CARDS_ERR = '\nDealt cards must be a Deck.\n'

NAME_ERR = '\nName must be a string.\n'

# user input error messages
USER_INPUT_ERR = '\nInputs must be strings with 2 or 3 characters.\n'

USER_NO_CARD_ERR = '\nYou do not have that card.\n'

USER_TRUMP_NOT_STARTED_ERR = f'\nTrump {SUITS[TRUMP_SUIT]} has not started yet.\n'

USER_ROUND_SUIT_ERR = f'\nSelected card must be in round suit.\n'

# messages to user
INSTRUCTIONS = """
--------------
 INSTRUCTIONS
--------------
When it is your turn, please choose a card to play. 
Input must be a string of rank, followed by suit. 
e.g. 'qd' = queen of diamonds, '10s' = 10 of spades.

Cards placed on the pile will be in blue font.

The trump suit and the player to start the first round are chosen at random.
"""

USER_PROMPT = '\n> Choose a card: '

FINAL_SCORE_HEADER = """
-------------
 FINAL SCORE
-------------
"""


# functions to return coloured text
def red(string):
	''' Returns the given string in red font '''
	return f'{Fore.RED}{string}{Style.RESET_ALL}'

def blue(string):
	''' Returns the given string in red font '''
	return f'{Fore.BLUE}{string}{Style.RESET_ALL}'

def green(string):
	''' Returns the given string in red font '''
	return f'{Fore.GREEN}{string}{Style.RESET_ALL}'