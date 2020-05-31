import constants as c
from random import shuffle, randint
from collections import UserList
from card import Card


# https://stackoverflow.com/questions/36688966/let-a-class-behave-like-its-a-list-in-python
class Deck(UserList):
    ''' A Deck is a list of Cards '''
    def __init__(self, cards=None, sort_cards=False):
        '''
        Creates a deck from optional input list of Cards.
        If empty list is passed, an empty Deck is created.
        If nothing is passed, a full sorted Deck is created.
        '''
        FULL_DECK = [Card(rank, suit) for rank in c.RANKS for suit in c.SUITS]

        if cards is None:
            cards = FULL_DECK
        else:
            cards = sorted(cards) if sort_cards else cards

        if not isinstance(cards, list) or not all(isinstance(c, Card) for c in cards):
            raise TypeError(c.red(c.DECK_INPUT_ERR))

        # UserList uses 'self.data' as variable name for built-in list functions
        self.data = cards


    def __repr__(self):
        return str(self.data)


    def __eq__(self, other, suit=None):
        ''' Returns True if both decks have the same strength. '''
        return self.get_strength() == other.get_strength()


    def __gt__(self, other, suit=None):
        ''' Returns True if first deck is stronger than second deck. '''
        return self.get_strength() > other.get_strength()


    def __lt__(self, other, suit=None):
        ''' Returns True if first deck is weaker than second deck. '''
        return self.get_strength() < other.get_strength()


    def get_cards_by_suit(self):
        '''
        Returns a dict of suits mapped to a sorted Deck of cards with that suit.
        '''
        cards_by_suit = {suit: [] for suit in c.SUITS}

        for card in self.data:
            cards_by_suit[card.suit].append(card)

        return {
            suit: Deck(cards, sort_cards=True)
            for suit, cards in cards_by_suit.items()
        }


    def get_strength(self):
        ''' Returns total card_strength of current Deck. '''
        return sum(card.card_strength for card in self.data)


    def pop_random_card(self):
        ''' Pops a random card from current Deck. '''
        return self.data.pop(randint(0, len(self.data)-1))


    def shuffle(self):
        ''' Shuffle all cards present in deck. '''
        shuffle(self.data)


    def deal(self, n, k=None, shuffle=False):
        '''
        n: number of players to deal to.
        k: number of cards to deal to each player. Default is None, meaning all cards are dealt.
        shuffle: whether to shuffle the deck before dealing. Default is False.

        Deal k cards each to n players. Deal all cards in deck if k unspecified.
        Returns a list of n Decks, each of which has k cards.
        '''
        if shuffle:
            shuffle(self.data)

        # if k is not specified, each player gets (num cards in deck / num players) cards
        k = int(len(self.data) / n) if k is None else k

        # will contain n Decks of k length each
        self.hands = []

        for i in range(n):
            hand = Deck(self.data[:k])  # get a Deck of k cards from current Deck
            self.hands.append(hand)
            self.data = self.data[k:]   # remove those k cards from current Deck

        return self.hands
