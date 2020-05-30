import constants as c
from random import choice
from deck import Deck
from player import BridgePlayer


class BridgeBot(BridgePlayer):
    ''' A Bot bridge player class which inherits from BridgePlayer. '''
    def __init__(self, dealt, num, name=None):
        '''
        dealt: a Deck of cards dealt to this player
        num: this player's player number
        name: an optional name field that defaults to f'Player {num}'
        '''
        super().__init__(dealt, num, name)

        # dict that maps other players numbers to cards they played.
        # starts with an empty Deck for everyone.
        self.seen = {p: Deck([]) for p in range(c.NUM_PLAYERS)}
        self.seen.pop(self.num)


    def play_card(self, round_suit=None):
        '''
        round_suit is None if player is starting the round.

        Naive approach used - comments inline.
        '''
        if round_suit is not None and round_suit.upper() not in c.SUITS:
            raise ValueError(c.red(c.SUIT_ERR))

        # if starting the round, play a random non-trump card if possible
        if round_suit is None:
            # try to pick a card that's not in c.TRUMP_SUIT
            try:
                # only suits with at least 1 card
                choices = [
                    s for s in self.hand
                    if self.hand[s] and s != c.TRUMP_SUIT
                ]
                
                random_suit = choice(choices)
            # except if only c.TRUMP_SUIT cards are left
            except IndexError:
                random_suit = c.TRUMP_SUIT
                c.TRUMP_STARTED = True

            card = self.hand[random_suit].pop_random_card()

        # if not starting the round
        else:
            # play highest card in sorted hand in round_suit if available
            if self.hand[round_suit]:
                card = self.hand[round_suit].pop(-1)
            # else play the smallest c.TRUMP_SUIT card if available
            elif self.hand[c.TRUMP_SUIT]:
                card = self.hand[c.TRUMP_SUIT].pop(0)
                c.TRUMP_STARTED = True
            # else play the smallest card in any other nonempty suit
            else:
                random_suit = choice([s for s in self.hand if self.hand[s]])
                card = self.hand[random_suit].pop(0)

        print(c.blue(f'{self.name} plays {card}'))

        return card


    def see_card(self, player, card):
        ''' Updates self.seen to include newly placed card by player. '''
        if player not in range(c.NUM_PLAYERS):
            raise ValueError(c.red(c.PLAYER_NUMBER_ERR))
        if not isinstance(card, Card):
            raise TypeError(c.red(c.CARD_CLASS_ERR))

        if player != self.num:
            self.seen[player].append(card)