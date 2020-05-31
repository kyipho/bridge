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

### Class attributes
Type `python` or `python3` in terminal first to start interpreter.

Create 2 cards, *2 of Clubs* and *Ace of Spades*, which are the smallest and largest cards in the game respectively:
```
>>> from card import Card
>>> c1 = Card('2', 'c')
>>> c2 = Card('a', 's')
```
Print them. Note that suits are converted to the suit characters when printing:
```
>>> print(c1, c2)
2♣ A♠
```
Get `Card.rank` and `Card.suit` attributes:
```
>>> print(c1.rank, c1.suit)
2 C
```
Get `Card.rank_strength`, which ranges from 1-13 ('2' is smallest, 'A' is largest):
```
>>> print(c1.rank_strength, c2.rank_strength)
1 13
```
Get `Card.suit_strength`, which ranges from 1-4 ('c' is smallest, 's' is largest):
```
>>> print(c1.suit_strength, c2.suit_strength)
1 4
```
Get `Card.card_strength`, which ranges from 1-52 (2 of Clubs is smallest, Ace of Spades is largest):
```
>>> print(c1.card_strength, c2.card_strength)
1 52
```
### Class functions
Compare cards based on `card_strength`:
```
>>> c1 > c2
False
>>> c1 < c2
True
>>> c1 == c2
False
```
A card's bridge strength varies from each round, depending on round suit and trump suit.
Bridge strengths range from 0 to 26. Use `Card.get_bridge_strength(round_suit, trump_suit)` to get the value.

Assuming round suit = 'h' and trump suit = 'c':
```
>>> c1.get_bridge_strength(round_suit='h', trump_suit='c')
14
>>> c2.get_bridge_strength(round_suit='h', trump_suit='c')
0

# note that c1 is stronger than ace of hearts this round
>>> Card('A', 'h').get_bridge_strength(round_suit='h', trump_suit='c')
13
```

## deck.py
Defines the Deck class for the game. A Deck is basically a list of Cards. Sample of how it works:

### Class attributes
Type `python` or `python3` in terminal first to start interpreter.

Create a full sorted Deck of Cards and get `Deck.data` (`data` variable name is inherited from superclass `UserList`):
```
>>> from deck import Deck
>>> sorted_full_deck = Deck()
>>> sorted_full_deck.data
[2♣, 2♦, 2♥, 2♠, 3♣, 3♦, 3♥, 3♠, 4♣, 4♦, 4♥, 4♠, 5♣, 5♦, 5♥, 5♠, 6♣, 6♦, 6♥, 6♠, 7♣, 7♦, 7♥, 7♠, 8♣, 8♦, 8♥, 8♠, 9♣, 9♦, 9♥, 9♠, 10♣, 10♦, 10♥, 10♠, J♣, J♦, J♥, J♠, Q♣, Q♦, Q♥, Q♠, K♣, K♦, K♥, K♠, A♣, A♦, A♥, A♠]
```

List (slicing, indexing etc.) and Card functionality is available:
```
>>> len(sorted_full_deck)
52
>>> print(sorted_full_deck[0:10])
[2♣, 2♦, 2♥, 2♠, 3♣, 3♦, 3♥, 3♠, 4♣, 4♦]
>>> print(sorted_full_deck[0].card_strength > sorted_full_deck[1].card_strength)
False
>>> Deck().pop(-1)
A♠
```
Create an **unsorted** Deck from an unsorted list of cards:
```
>>> list_of_cards = [Card('a', 'c'), Card('3', 'h'), Card('10', 'd'), Card('j', 's')]
>>> list_of_cards
[A♣, 3♥, 10♦, J♠]
>>> d1 = Deck(cards=list_of_cards)
>>> d1
[A♣, 3♥, 10♦, J♠]
```
Create a **sorted** Deck from an unsorted list of cards:
```
>>> d1_sorted = Deck(cards=list_of_cards, sort_cards=True)
>>> d1_sorted
[3♥, 10♦, J♠, A♣]
```

### Class functions
`Deck.get_strength()`: returns total `card_strength` of current Deck.
For a full Deck, total `card_strength` should be `1+2+3+...+51+52 = 53*26 = 1378`.
```
>>> sorted_full_deck.get_strength()
1378
>>> d1.get_strength()
130
```
Compare strength of various Decks based on `get_strength()`:
```
>>> sorted_full_deck > d1
True
>>> sorted_full_deck < d1
False
>>> sorted_full_deck == d1
False
```
`Deck.pop_random_card()`: Chooses a random Card from Deck.
```
>>> Deck().pop_random_card()
3♠
>>> Deck().pop_random_card()
J♥
>>> Deck().pop_random_card()
5♦
```
`Deck.shuffle()`: Shuffles Deck in-place.
```
>>> d1_sorted
[3♥, 10♦, J♠, A♣]
>>> d1_sorted.shuffle()
>>> d1_sorted
[3♥, J♠, A♣, 10♦]
```
`Deck.deal(n, k=None, shuffle=False)`:
  - n: number of players to deal to.
  - k: number of cards to deal to each player. Default is None i.e. all cards are dealt.
  - shuffle: whether to shuffle the deck before dealing. Default is False.

Returns a list of n Decks, each of which has k cards.

From an unshuffled Deck, deal all cards to 4 players like in a typical Bridge game:
```
>>> hands = sorted_full_deck.deal(n=4, k=None, shuffled=True)
>>> for i in range(len(hands)):
...     print(f'Hand {i}: {hands[i]}')
...
Hand 0: [9♣, Q♥, 3♦, 7♠, K♣, 9♦, 2♣, 10♣, 3♠, 4♥, Q♦, 6♥, A♦]
Hand 1: [10♦, 3♥, 10♥, J♦, K♠, A♣, 7♥, 4♦, K♥, 7♦, 2♠, 5♠, A♠]
Hand 2: [Q♣, 2♥, 8♣, 8♦, J♠, 5♦, 8♠, Q♠, 4♠, 4♣, 5♥, A♥, J♥]
Hand 3: [6♦, J♣, 8♥, 2♦, 5♣, 6♣, 6♠, 3♣, K♦, 7♣, 10♠, 9♥, 9♠]
```
Create a full Deck, shuffle it, then deal 2 cards each to 7 players:
```
>>> d = Deck()
>>> d.shuffle()
>>> d
[K♠, 4♣, J♣, A♥, 8♣, 3♣, 4♠, K♦, K♥, 9♣, A♣, 3♥, 2♦, J♠, 5♥, 2♥, 6♣, A♠, Q♠, 7♥, 6♠, 7♠, A♦, 10♦, 10♠, 6♦, 5♦, 4♥, J♥, Q♦, 9♠, 3♦, 5♣, 5♠, 8♥, K♣, 4♦, 8♠, 6♥, 10♥, 9♦, 7♣, Q♣, 10♣, 2♣, J♦, 3♠, 7♦, Q♥, 2♠, 8♦, 9♥]
>>> hands = d.deal(n=7, k=2, shuffle=False)
>>> hands
[[K♠, 4♣], [J♣, A♥], [8♣, 3♣], [4♠, K♦], [K♥, 9♣], [A♣, 3♥], [2♦, J♠]]
>>> len(d)
38
```
