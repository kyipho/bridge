# Bridge
Python files for 1 user to play a game of Bridge against 3 bots in the command line. Just a small project so I can learn some OOP concepts.

*Disclaimers:*
- *The game here is not based off any official Bridge rules.*
- *There is no concept of partnership / bidding in the game right now (i.e. battle royale).*
- *'No trump' is not included in the game right now.*
- *The bots play cards using only a naive algorithm - no AI whatsoever.*
  
# Starting the game
1. Download Python3 (https://www.python.org/downloads/) if you haven't.
2. Download these files into a directory of your choice (e.g. Desktop)
3. Open Terminal / Command Line and navigate into that directory: `cd desktop`
4. Start the game using: `python bridge_game.py` (Might have to use `python3` for Macs)

# Files
## constants.py
Defines some constants, including the ranks and suits for playing cards:

`RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']`

`SUITS = {'C': '♣', 'D': '♦', 'H': '♥', 'S': '♠'}`

`...`

## card.py
Defines the Card class for the game. Sample of how it works:

```
# type `python` or `python3` in terminal first to start interpreter
>>> from card import Card

# smallest card in the game: 2 of clubs
>>> c1 = Card('2', 'c')

# largest card in the game: ace of spades
>>> c2 = Card('a', 's')

# suits are converted to the suit characters when printing
>>> print(c1, c2)
2♣ A♠

>>> print(c1.rank, c1.suit)
2 C

# rank_strengths range from 1-13 ('2' is smallest, 'A' is largest)
>>> print(c1.rank_strength, c2.rank_strength)
1 13

# suit_strengths range from 1-4 ('c' is smallest, 's' is largest)
>>> print(c1.suit_strength, c2.suit_strength)
1 4

# overall card strengths range from 1 to 52:
>>> print(c1.card_strength, c2.card_strength)
1 52

# card comparison
>>> c1 > c2
False
>>> c1 < c2
True
>>> c1 == c2
False

###
a card's bridge strength varies from each round, depending on round suit and trump suit.
Bridge strengths range from 0 to 26.
Assuming round suit = 'h' and trump suit = 'c':
###
>>> c1.get_bridge_strength(round_suit='h', trump_suit='c')
14
>>> c2.get_bridge_strength(round_suit='h', trump_suit='c')
0

# c1 is stronger than ace of hearts this round
>>> Card('A', 'h').get_bridge_strength(round_suit='h', trump_suit='c')
13
```

# WIP