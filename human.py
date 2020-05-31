import constants as c
from pprint import pprint
from card import Card
from player import BridgePlayer

class BridgeHuman(BridgePlayer):
    ''' A human bridge player class which inherits from Player. '''
    def __init__(self, dealt, num, name=None):
        '''
        dealt: a Deck of cards dealt to this player
        num: this player's player number
        name: an optional name field that defaults to f'Player {num}'
        '''
        super().__init__(dealt, num, name)


    def play_card(self, round_suit=None):
        '''
        Takes user input to play a card. 
        round_suit is None if starting the round.
        '''
        if round_suit is not None and round_suit.upper() not in c.SUITS:
                raise ValueError(c.red(c.SUIT_ERR))

        # show user's cards on the screen (a dict of suits to cards)
        print('\nYour hand:\n')
        pprint(self.hand)

        # prompt user for input
        while True:
            user_input = input(c.USER_PROMPT).upper()

            # check input for type errors
            if not isinstance(user_input, str) or len(user_input) < 2:
                print(c.red(c.USER_INPUT_ERR))
                continue

            user_rank = user_input[:-1]
            user_suit = user_input[-1]

            # check if inputs are valid ranks and suits
            if user_rank not in c.RANKS or user_suit not in c.SUITS:
                print(c.red(c.RANK_ERR))
                print(c.red(c.SUIT_ERR))
                continue

            # selected card
            card = Card(user_rank, user_suit)

            # error if user does not have that card
            if card not in self.hand[card.suit]:
                print(c.red(c.USER_NO_CARD_ERR))
                continue

            # if user is starting the round
            if round_suit is None:
                # error if user is playing a trump card when not c.TRUMP_STARTED
                if card.suit == c.TRUMP_SUIT and not c.TRUMP_STARTED:
                    print(c.red(c.USER_TRUMP_NOT_STARTED_ERR))
                    continue

            # if user is not starting the round and card.suit != round_suit
            if round_suit is not None and card.suit != round_suit:
                # error if user still has a card in round_suit
                if len(self.hand[round_suit]) > 0:
                    print(c.red(c.USER_ROUND_SUIT_ERR))
                    print(c.red(f'Round suit: {c.SUITS[round_suit]}'))
                    continue

                # if user plays a trump card, c.TRUMP_STARTED = True
                if card.suit == c.TRUMP_SUIT and not c.TRUMP_STARTED:
                    c.TRUMP_STARTED = True

            # checks complete and chosen card is valid
            break

        # remove card from user's hand
        self.hand[card.suit].remove(card)

        print(c.yellow(f'\n{self.name} plays {card}'))

        return card
