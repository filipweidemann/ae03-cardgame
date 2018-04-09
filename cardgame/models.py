from random import randint

class Card:
    def __init__(self, value):
        self.value = value


class Hand:
    def __init__(self, quantity):
        self.cards = []
        self.quantity = quantity

    def discard(self):
        return self.cards.pop()

    def generate(self):
        for x in range(0, self.quantity):
            self.cards.append(Card(randint(0, 10)))
        return self

class Table:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def assign_to_winner(self):
        winner = max(self.cards, key=lambda x: x[0])[1]
        winner.stack.append(self.cards)

class Player:
    def __init__(self, table, name):
        self.hand = None
        self.name = name
        self.stack = []
        self.table = table
        self.winner = False

    def get_hand(self, value):
        self.hand = Hand(value).generate()

    def drop(self):
        self.table.add_card((self.hand.discard().value, self))



class Game:
    def __init__(self, table, players, hand_quantity):
        self.hand_quantity = hand_quantity
        self.table = table
        self.players = players
        self.round = 0

    def prepare_game(self):
        for player in self.players:
            player.get_hand(self.hand_quantity)

    def determine_winner(self):
        players = [player for player in self.players]
        winner = max(players, key=lambda x: x.stack)
        print(winner.name)

    def play(self):
        while self.round < self.hand_quantity:
            for player in self.players:
                player.drop()
            self.table.assign_to_winner()
            self.round += 1
        self.determine_winner()
