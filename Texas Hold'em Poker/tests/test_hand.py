import unittest
from poker.card import Card
from poker.hand import Hand

class HandTest(unittest.TestCase):
	def test_receives_and_stores_cards(self):
		cards = [Card(rank = 'Ace', suit = 'Spades'),
				Card(rank = '6', suit = 'Clubs')]
		hand = Hand(cards = cards)
		
		self.assertEqual(hand.cards, cards)

	def test_figures_out_high_card_is_best_rank(self):
		cards = [Card(rank = 'Ace', suit = 'Diamonds'),
				Card(rank = '7', suit = 'Clubs')]
		hand = Hand(cards = cards)

		self.assertEqual(hand.best_rank(), 'High Card')

	def test_figures_out_pair_is_best_rank(self):
		cards = [Card(rank = 'Ace', suit = 'Spades'),
				Card(rank = 'Ace', suit = 'Clubs')]
		hand = Hand(cards = cards)

		self.assertEqual(hand.best_rank(), 'Pair')