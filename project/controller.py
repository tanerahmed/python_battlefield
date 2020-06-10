from project.player.player_repository import PlayerRepository
from project.card.card_repository import CardRepository
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.card.magic_card import MagicCards
from project.card.trap_card import TrapCard
from project.battle_field import BattleField


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, player_type: str, username: str):
        player = Advanced(username) if player_type == 'Advance' else Beginner(username)
        self.player_repository.add(player)
        return f'Successfully add player of type{player_type} with username {username}'

    def add_card(self, card_type: str, name: str):
        card = MagicCards(name) if card_type == "Magic" else TrapCard(name)
        self.card_repository.add(card)
        return f"Successfully added cart of type {card_type}Card with name {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user {username}"

    def fight(self, attacker_name: str, enemy_name: str):
        attacker = self.player_repository.find(attacker_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ''
        for player in self.player_repository.players:
            result += f"Username: {player.username} - Health {player.health} - Cards {player.card_repository.count}\n"
            for card in player.card_repository.cards:
                result += f"### Carde: {card.name} - Damage: {card.damage_points}\n"
        return result

