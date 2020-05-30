import constants as c
from deck import Deck

class BridgePlayer():
    ''' A bridge player class. '''
    def __init__(self, dealt, num, name=None):
        '''
        dealt: a Deck of cards dealt to this player
        num: this player's player number, which ranges from 0 to 3
        name: an optional name field that defaults to f'Player {num}'
        '''
        if not isinstance(dealt, Deck):
            raise TypeError(c.red(c.DEALT_CARDS_ERR))
        if num not in range(4):
            raise ValueError(c.red(c.PLAYER_NUMBER_ERR))
        if name is not None and not isinstance(name, str):
            raise TypeError(c.red(c.NAME_ERR))

        self.num = num

        self.name = name if name is not None else f'Player {num}'

        # split dealt cards up into a dict of {suit: cards}
        self.hand = dealt.get_cards_by_suit()

        # number of sets this player has won
        self.score = 0


    def __repr__(self):
        return str(self.hand)