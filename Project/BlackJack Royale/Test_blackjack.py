import unittest
from unittest.mock import MagicMock, patch
import blackjack  

class TestBlackjack(unittest.TestCase):

    def test_load_images(self):
        card_images = []
        blackjack.load_images(card_images)  
        self.assertGreater(len(card_images), 0)

    def test_deal_card(self):
        frame_mock = MagicMock()
        blackjack.deck = [(1, 'image')]  
        initial_deck_length = len(blackjack.deck) 
        card = blackjack._deal_card(frame_mock) 
        self.assertEqual(len(blackjack.deck), initial_deck_length)

    def test_score_hand(self):
        hand1 = [(2, ''), (4, '')] 
        hand2 = [(10, ''), (1, '')]  
        hand3 = [(10, ''), (10, ''), (1, '')]  
        self.assertEqual(blackjack.score_hand(hand1), 6)  
        self.assertEqual(blackjack.score_hand(hand2), 21) 
        self.assertEqual(blackjack.score_hand(hand3), 21)  

    def test_deal_dealer(self):
        blackjack.dealer_hand = [(10, ''), (10, '')] 
        blackjack.player_hand = [(10, ''), (10, '')] 
        with patch('blackjack.deal_player'):
            blackjack.deal_dealer()  
        self.assertGreaterEqual(len(blackjack.dealer_hand), 2) 

    def test_deal_player(self):
        player_card_frame_mock = MagicMock()
        player_score_label_mock = MagicMock()
        blackjack.deck = [(2, ''), (3, '')] 
        blackjack.deal_player() 
        self.assertGreaterEqual(len(blackjack.player_hand), 1)

    def test_initial_deal(self):
        blackjack.dealer_card_frame = MagicMock()
        blackjack.player_card_frame = MagicMock()
        blackjack.result_text = MagicMock()
        blackjack.deal_player = MagicMock()
        blackjack.deck = [(2, ''), (3, ''), (4, ''), (5, '')]
        with patch('blackjack._deal_card') as mock_deal_card: 
            mock_deal_card.side_effect = [(2, ''), (3, '')]  
        try:
            blackjack.initial_deal()
            self.assertTrue(True) 
        except:
            self.fail("initial_deal() raised an unexpected error!")

    def test_new_game(self):
        blackjack.dealer_card_frame = MagicMock()
        blackjack.player_card_frame = MagicMock()
        blackjack.result_text = MagicMock()
        blackjack.initial_deal = MagicMock()
        blackjack.deck = [(2, ''), (3, ''), (4, ''), (5, '')]
        initial_deck_length = len(blackjack.deck)
        blackjack.new_game()  
        self.assertEqual(len(blackjack.dealer_hand), 0) 
        self.assertEqual(len(blackjack.player_hand), 0)  
        self.assertEqual(len(blackjack.deck), initial_deck_length) 

    def test_shuffle(self):
        blackjack.deck = [(2, ''), (3, ''), (4, ''), (5, '')] 
        initial_deck_order = blackjack.deck[:]
        blackjack.shuffle()  
        self.assertNotEqual(blackjack.deck, initial_deck_order)  

if __name__ == '__main__':
    unittest.main()
