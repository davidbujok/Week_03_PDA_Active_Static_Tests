import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_1 = Card("clubs", 8)
        self.card_2 = Card("diamonds", 4)
        self.card_3 = Card("hearts", 9)
        self.card_4 = Card("spades", 1)
        self.game = CardGame()
        self.cards = [self.card_1, self.card_2, self.card_3, self.card_4]

    def test_ace_is_one(self):
        self.assertEqual(True, self.game.check_for_ace(self.card_4))
    
    def test_higher_card(self):
        self.assertEqual(self.card_3, self.game.highest_card(self.card_4, self.card_3))

    def test_total_points_in_cards(self):
        self.assertEqual(22, self.game.cards_total(self.cards))
