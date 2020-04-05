import unittest
import random
from core.round import TNRoundState, PHASES

random.seed(0)


class TestRound(unittest.TestCase):

    def setUp(self):
        self.round = TNRoundState()

    def test_deck_deal(self):
        self.round._start_bidding()
        for player_deck in self.round.player_decks:
            self.assertEqual(len(player_deck.cards), 4)
        self.round._start_game()
        for player_deck in self.round.player_decks:
            self.assertEqual(len(player_deck.cards), 8)

    def test_bidding_1(self):
        self.round._start_bidding()

        # False Bid
        self.round.place_bid(0, 16)
        self.assertEqual(self.round.bids, [0, 0, 0, 0])

        # 1 bids 16
        self.round.place_bid(1, 16)
        self.assertEqual(self.round.bids, [0, 16, 0, 0])
        self.assertEqual(self.round.initiator_bidder, 1)
        self.assertEqual(self.round.challenging_bidder, 2)

        # 2 tries matching from challenger level
        self.round.place_bid(2, 16)
        self.assertEqual(self.round.bids, [0, 16, 0, 0])
        self.assertEqual(self.round.highest_bidder, 1)
        self.assertEqual(self.round.initiator_bidder, 1)
        self.assertEqual(self.round.challenging_bidder, 2)

        # 2 bids 17
        self.round.place_bid(2, 17)
        self.assertEqual(self.round.bids, [0, 16, 17, 0])
        self.assertEqual(self.round.highest_bidder, 2)
        self.assertEqual(self.round.initiator_bidder, 1)
        self.assertEqual(self.round.challenging_bidder, 2)

        # 1 bids 17
        self.round.place_bid(1, 17)
        self.assertEqual(self.round.bids, [0, 17, 17, 0])
        self.assertEqual(self.round.highest_bidder, 1)
        self.assertEqual(self.round.initiator_bidder, 1)
        self.assertEqual(self.round.challenging_bidder, 2)

        # 2 pass
        self.round.place_bid(2, 0)
        self.assertEqual(self.round.bids, [0, 17, 17, 0])
        self.assertEqual(self.round.highest_bidder, 1)
        self.assertEqual(self.round.initiator_bidder, 1)
        self.assertEqual(self.round.challenging_bidder, 3)

        # False Bid
        self.round.place_bid(2, 0)
        self.assertEqual(self.round.bids, [0, 17, 17, 0])
        self.assertEqual(self.round.highest_bidder, 1)
        self.assertEqual(self.round.initiator_bidder, 1)
        self.assertEqual(self.round.challenging_bidder, 3)

        # 3 tries matching from challenger level
        self.round.place_bid(3, 17)
        self.assertEqual(self.round.bids, [0, 17, 17, 0])
        self.assertEqual(self.round.highest_bidder, 1)
        self.assertEqual(self.round.initiator_bidder, 1)
        self.assertEqual(self.round.challenging_bidder, 3)

        # 3 bids 18
        self.round.place_bid(3, 18)
        self.assertEqual(self.round.bids, [0, 17, 17, 18])
        self.assertEqual(self.round.highest_bidder, 3)
        self.assertEqual(self.round.initiator_bidder, 1)
        self.assertEqual(self.round.challenging_bidder, 3)

        # 1 passes
        self.round.place_bid(1, 0)
        self.assertEqual(self.round.bids, [0, 17, 17, 18])
        self.assertEqual(self.round.highest_bidder, 3)
        self.assertEqual(self.round.initiator_bidder, 3)
        self.assertEqual(self.round.challenging_bidder, 0)

        # False Bid
        self.round.place_bid(0, 6)
        self.assertEqual(self.round.bids, [0, 17, 17, 18])
        self.assertEqual(self.round.highest_bidder, 3)
        self.assertEqual(self.round.initiator_bidder, 3)
        self.assertEqual(self.round.challenging_bidder, 0)

        # 0 passes
        self.round.place_bid(0, 0)
        self.assertEqual(self.round.bids, [0, 17, 17, 18])
        self.assertEqual(self.round.highest_bidder, 3)
        self.assertEqual(self.round.initiator_bidder, 3)
        self.assertEqual(self.round.challenging_bidder, 0)

        # Check Phases
        self.assertNotEqual(self.round.phase, PHASES.BIDDING)
        self.assertEqual(self.round.phase, PHASES.TRUMP_SETTING)


if __name__ == '__main__':
    unittest.main()
