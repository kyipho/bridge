import constants as c

class Card:
    '''
    Card(rank: str, suit: str). Rank and suit inputs are not case-sensitive.

    Examples:
        Card('2', 'd') gives 2♦
        Card('k', 'c') gives K♣
    '''
    def __init__(self, rank, suit):
        if rank.upper() not in c.RANKS:
            raise ValueError(c.red(c.RANK_ERR))
        if suit.upper() not in c.SUITS:
            raise ValueError(c.red(c.SUIT_ERR))

        self.rank = rank.upper()
        self.suit = suit.upper()

        self.rank_strength = c.RANK_STRENGTHS[self.rank]
        self.suit_strength = c.SUIT_STRENGTHS[self.suit]

        # overall card strength = (4 * rank_strength + 1 * suit_strength) - 4
        # -4 so that card strength ranges from 1 to 52, instead of 5 to 56.
        self.card_strength = (4 * self.rank_strength + 1 * self.suit_strength) - 4


    def __repr__(self):
        ''' Prints a card's rank and suit e.g. K♣ '''
        return f'{self.rank}{c.SUITS[self.suit]}'


    def __eq__(self, other):
        ''' Returns True if both cards have the same card strength '''
        return self.card_strength == other.card_strength


    def __gt__(self, other):
        ''' Returns True if first card is stronger than second card '''
        return self.card_strength > other.card_strength


    def __lt__(self, other):
        ''' Returns True if first card is weaker than second card '''
        return self.card_strength < other.card_strength


    def get_bridge_strength(self, round_suit):
        '''
        Returns card bridge strength for a given round of Bridge.
        Bridge strengths range from 0 to 26:
            - 0 if self.suit not in [round_suit, c.TRUMP_SUIT]
            - 1 to 13: rank_strength if self.suit == round_suit
            - 14 to 26: rank_strength if self.suit == trump.suit
        '''
        if self.suit not in [round_suit, c.TRUMP_SUIT]:
            return 0
        elif self.suit == round_suit:
            return self.rank_strength
        elif self.suit == c.TRUMP_SUIT:
            return 13 + self.rank_strength
