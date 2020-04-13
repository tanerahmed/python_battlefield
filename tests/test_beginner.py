import unittest
from project.player.beginner import Beginner


class TestAdvancePlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Beginner('Peter')

    def test_init_should_create_player_attributes(self):
        self.assertEqual(self.player.username, "Peter")
        self.assertEqual(self.player.health, 50)
        self.assertEqual(self.player.card_repository.__class__.__name__, "CardRepository")


