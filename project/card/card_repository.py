from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.cards = []

    @property
    def count(self):
        return len(self.cards)

    def add(self, card: Card):
        # if card.name == self.cards
        if any(card.name == cr.name for cr in self.cards):
            raise ValueError(f'Card {card.name} already exit')
        self.cards.append(card)

    def remove(self, card_name: str):
        if card_name == '':
            raise ValueError("Card cannot be empty string.")
        found_card = self.find(card_name)
        self.cards.remove(found_card)

    def find(self, name: str):
        found_card = [c for c in self.cards if c.name == name][0]
        return found_card
