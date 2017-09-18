# Do not change import statements.
import unittest
from SI507F17_project1_cards import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in the code
# description file works as that file says.
# If you have correctly written the tests, at least 3 tests
# should fail. If more than 3 tests
# fail, it should be because multiple of the test methods address
# the same problem in the code.
# You may write as many TestSuite subclasses as you like, but
# you should try to make these tests
# well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)


###########


class TestCard(unittest.TestCase):
	def test_suitstring(self):
        c = Card(1, 5)
        a = c.suit
        self.assertEqual(type(a), type("word"), "check suit returns string")

    def test_cardrank(self):
        c = Card(2, 13)
        self.assertEqual(c.rank, "King", "check that rank is King when 12")

    def test_cardrank2(self):
        c = Card(3, 4)
        self.assertEqual(c.rank, 4, "check rank is an integer")

    def test_cardranknum(self):
        c = Card(1, 11)
        self.assertEqual(type(c.rank_num), type(5), "Rank_num is an integer")

    def test_strcard(self):
        c = Card(0, 1)
        self.assertEqual(str(c), "Ace of Diamonds", "Print reflects Card int")

    def test_carddefault(self):
        c = Card()
        self.assertEqual(str(c), "2 of Diamonds", "Card's defaults are 0, 2")


class TestDeck(unittest.TestCase):
    def test_deckcards(self):
        d = Deck()
        self.assertEqual(type(d.cards), type([1, 2, 12]), "Cards is a list")

    def test_decknumcards(self):
        d = Deck()
        self.assertEqual(len(d.cards), 52, "52 cards in the list")

    def test_popcard(self):
        d = Deck()
        d_removed = d.pop_card(1)
        self.assertEqual(len(d_removed.cards), 51, "pop_card removes one card")

    def test_replacecardmethod(self):
        d = Deck()
        a = d.replace_card(Card(2, 13))
        self.assertEqual(d, a, "Deck does not change with replace_card")

    def test_dealhand(self):
        d = Deck()
        a = d.deal_hand(52)
        self.assertTrue(len(a) == 52)

    def test_sortcard(self):
        d = Deck()
        a = d.sort_cards
        self.assertIsNotEqual(d[0], a[0], "First element in list has changed")


class TestPlayWarGame(unittest.TestCase):
    def test_scores(self):
        a = play_war_game(testing=True)
        if a[0] == "Tie":
            self.assertEqual(a[1], a[2], "Equal scores returns True")

    def test_scores1(self):
        a = play_war_game(testing=True)
        if a[0] == "Player1":
            self.assertTrue(a[1] > a[2])

    def test_scores2(self):
        a = play_war_game(testing=True)
        if a[0] == "Player2":
            self.assertTrue(a[2] > a[1])


class TestShowSong(unittest.TestCase):
    def test_songinstance(self):
        a = show_song()
        self.assertEqual(type(a), type(Card()), "Function returns instance")

unittest.main(verbosity=2)
