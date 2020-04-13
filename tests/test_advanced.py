import unittest
from project.player.advanced import Advanced


class TestAdvancePlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Advanced('Peter')

    def test_init_should_create_player_attributes(self):
        self.assertEqual(self.player.username, "Peter")
        self.assertEqual(self.player.health, 250)
        self.assertEqual(self.player.card_repository.__class__.__name__, "CardRepository")

    def test_set_username__with_empty_username__should_raise_error(self):
        with self.assertRaises(ValueError) as context:
            self.player.username = ''
        self.assertIsNotNone(context.exception)

    def test_set_health__with_less_than_zero__should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.player.health = -1
        self.assertEqual(str(cm.exception), "Player's health bonus cannot be less than zero.")

    def test_take_damage__with_less_than_zero__should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.player.take_damage(-1)
        self.assertIsNotNone(cm.exception)

    def test_take_damage__with_correct_value__should_reduce_health_with_the_value(self):
        expected = 50
        self.player.take_damage(200)
        actual = self.player.health
        self.assertEqual(actual, expected)

    def test_is_dead__should_return_true(self):
        self.player.health = 0
        actual = self.player.is_dead
        self.assertTrue(actual)

    def test_is_dead__should_return_false(self):
        actual = self.player.is_dead
        self.assertFalse(actual)


