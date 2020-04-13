from project.player.player import Player


class BattleField:

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead")

        if attacker.__class__.__name__ == "Beginner":
            self.__bonus_increase_player_health(attacker)
            self.__bonus_increase_player_cards_damage_points(attacker)

        if enemy.__class__.__name__ == "Beginner":
            self.__bonus_increase_player_health(enemy)
            self.__bonus_increase_player_cards_damage_points(enemy)

        self.__bonus_for_player(attacker)
        self.__bonus_for_player(enemy)

        # First attack ATTACKER
        self.__hit(attacker, enemy)

        # Second attack Enemy
        self.__hit(enemy, attacker)

    def __bonus_increase_player_health(self, player):
        player.health += 40

    def __bonus_increase_player_cards_damage_points(self, player):
        for card in player.card_repository.cards:
            card.damage_points += 30

    def __bonus_for_player(self, player):
        player.health += sum(card.health_points for card in player.card_repository.cards)

    def __hit(self, fighter, victim):
        for card in fighter.card_repository.cards:
            victim.take_damage(card.damage_points)



