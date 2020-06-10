from project.player.player import Player
from project.player.advanced import Advanced


class PlayerRepository:

    def __init__(self):
        self.players = []

    @property
    def count(self):
        return len(self.players)

    def add(self, player: Player):
        # if any(player.username == p.username for p in self.players):
        if player.username in [p.username for p in self.players]:
            raise ValueError(f"Player {player.username} already exist")
        self.players.append(player)

    def remove(self, player_name: str):
        if player_name == '':
            raise ValueError('Player cannot be empty string')

        found_player = self.find(player_name)
        self.players.remove(found_player)

    def find(self, username):
        try:
            found_player = [player for player in self.players if player.username == username][0]
        except IndexError:
            raise IndexError('No player found!')

        return found_player
