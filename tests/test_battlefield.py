import unittest
from project.battle_field import BattleField
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.card.trap_card import TrapCard
from project.card.magic_card import MagicCards


class TestBattleField(unittest.TestCase):

    def setUp(self) -> None:
        self.battlefield = BattleField()

    def test_fight_with_one_of_player_is_dead__should_raise_error(self):
        attacker = Advanced('Attacker')
        enemy = Beginner('Enemy')
        attacker.health = 0
        with self.assertRaises(ValueError) as cm:
            self.battlefield.fight(attacker, enemy)
        self.assertIsNotNone(cm.exception)

    def test_fight__when_player_is_beginner__should_increase_health(self):
        beginner = Beginner('Beginner')
        advance = Advanced("Advanced")
        expected = 50 + 40
        self.battlefield.fight(beginner, advance)
        actual = beginner.health
        self.assertEqual(actual, expected)

    def test_fight__when_player_is_beginner__should__increase_his_cards_damage_points(self):
        beginner = Beginner('Beginner')
        advance = Advanced("Advanced")
        magic_card = MagicCards('my_magic')

        beginner.card_repository.add(magic_card)
        # test player health is increase
        expected_health = 50 + 40 + 80
        self.battlefield.fight(beginner, advance)
        actual_health = beginner.health
        # test player cards is increase
        expected_card_damage_point = 5 + 30
        actual_card_damage_point = beginner.card_repository.cards[0].damage_points

        self.assertEqual(expected_health, actual_health)
        self.assertEqual(actual_card_damage_point, expected_card_damage_point)

    # def test_fight__should_decrease_players_health(self):
    #     attacker = Beginner('Beginner')
    #     enemy = Advanced("Advanced")
    #     magic_card = MagicCards('my_magic')
    #
    #     attacker.card_repository.add(magic_card)
    #     enemy.card_repository.add(magic_card)
    #
    #     # first hit attacker
    #     attacker_health_before_fight = 170
    #     enemy_health_before_fight = 250
    #
    #     self.assertEqual(attacker.health, 165)