import enum
from core.deck import Deck
TN_NUMBERS = ['J', '9', 'A', '10', 'K', 'Q', '8', '7']
TN_SUITES = ['D', 'C', 'H', 'S']
BID_MIN = 16
BID_MAX = 28


class PHASES(enum.Enum):
    NOT_STARTED = 1
    BIDDING = 2
    TRUMP_SETTING = 3
    GAME = 4
    GAME_OVER = 5


class TNRoundState:
    def __init__(self, dealer=0):
        self.main_deck = Deck.create_shuffled_deck(TN_SUITES, TN_NUMBERS)
        self.player_decks = [Deck.create_empty_deck() for _ in range(4)]
        
        self.dealer = dealer
        self.points = [0 for _ in range(2)]
        
        # Set Phase
        self.phase = PHASES.NOT_STARTED

    def _start_bidding(self):
        self.bids = [0 for _ in range(4)]
        self.initiator_bidder = (self.dealer + 1) % 4
        self.challenging_bidder = (self.dealer + 2) % 4
        self.initiator_turn = True
        self.bidding_over = False
        self.highest_bidder = 0

        # Give four cards to each player
        [deck.aquire(self.main_deck.deal(4)) for deck in self.player_decks]
        self.phase = PHASES.BIDDING

    def _start_game(self):
        # Give four cards to each player
        [deck.aquire(self.main_deck.deal(4)) for deck in self.player_decks]
        self.phase = PHASES.GAME

    def place_bid(self, player_idx, bid):
        if self.phase == PHASES.BIDDING:
            pass_flag = False
            # Initiator plays in turn
            if (player_idx == self.initiator_bidder and self.initiator_turn):
                # Initiator Passes
                if (bid == 0):
                    self.initiator_bidder = self.challenging_bidder
                    self.challenging_bidder = (self.challenging_bidder + 1) % 4
                    pass_flag = True
                # Initiator Bids
                if (bid >= max(self.bids)):
                    self.bids[self.initiator_bidder] = bid
                    self.highest_bidder = self.initiator_bidder
                    self.initiator_turn = not self.initiator_turn
            # Challenger plays in turn
            elif (player_idx == self.challenging_bidder and (not self.initiator_turn)):
                # Challenger Passes
                if (bid == 0):
                    self.challenging_bidder = (self.challenging_bidder + 1) % 4
                    pass_flag = False
                # Challenger Bids
                if (bid > max(self.bids)):
                    self.bids[self.challenging_bidder] = bid
                    self.highest_bidder = self.challenging_bidder
                    self.initiator_turn = not self.initiator_turn

            if (pass_flag and self.challenging_bidder == self.dealer):
                self.phase = PHASES.TRUMP_SETTING

    def set_trump(self, player_idx, suit):
        if self.phase == PHASES.TRUMP_SETTING:
            if (player_idx == self.highest_bidder and suit in TN_SUITES):
                self.trump = suit
                self._start_game()

    def play_card(self, player_idx, card):
        if self.phase == PHASES.GAME:
            pass