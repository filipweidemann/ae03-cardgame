from random import randint

"""
    Card class storing a value
    
    :param value: the integer value of the card
"""
class Card:
    def __init__(self, value):
        self.value = value


"""
    Hand class storing cards for Players
    
    :param cards: list of card objects
    :param quantity: the amount of cards used to generate a hand
"""
class Hand:
    def __init__(self, quantity):
        self.cards = []
        self.quantity = quantity

    # discard the top most Card on the Hand
    def discard(self):
        return self.cards.pop()

    # generate a new Hand with :param quantity: cards in it.
    # shuffling is not required because Hand creation
    # already spawns random Cards
    def generate(self):
        for x in range(0, self.quantity):
            self.cards.append(Card(randint(0, 10)))
        return self


"""
    Table class used to assign Players to games
    
    :param cards: list of cards laying on the table used for winner checking
"""
class Table:
    def __init__(self):
        self.cards = []

    # add a (Card, Player) tuple to the list
    def add_card(self, card):
        self.cards.append(card)

    # determine the winner based on Cards
    # on the Table
    def assign_to_winner(self):
        # get the winning Card
        winner_card = max(self.cards, key=lambda x: x[0])

        # check if the table only contains cards with the same value
        same_cards = [card for card in self.cards if card[0] == winner_card[0]]

        # if other cards have indeed the same value;
        # return without assigning a winner and start a new round
        if len(same_cards) > 1:
            return

        # if it is indeed the highest card,
        # assign the winner accordingly
        winner = winner_card[1]

        # give all cards to the winner
        for card in self.cards:
            winner.stack.append(card[0])

        # clear the table
        self.cards = []


"""
    Player class
    
    :param hand: Hand object 
    :param name: string containing the name of the player
    :param stack: list of cards obtained by winning rounds
    :param table: Table object on which the Player is currently playing
"""
class Player:
    def __init__(self, table, name):
        self.hand = None
        self.name = name
        self.stack = []
        self.table = table
        self.winner = False

    # generate a new Hand
    def get_hand(self, value):
        self.hand = Hand(value).generate()

    # get the top most card and throw it onto the Table
    def drop(self):
        self.table.add_card((self.hand.discard().value, self))



"""
    Game class used to keep track of players, tables and which round is currently being active
    
    :param hand_quantity: integer value of the quantity of Cards per Hand
    :param table: Table object on which the Game is currently being played
    :param players: list of Player objects
    :param round: integer value to keep track of the current round
"""
class Game:
    def __init__(self, table, players, hand_quantity):
        self.hand_quantity = hand_quantity
        self.table = table
        self.players = players
        self.round = 0

    # generate Hands for each player before game starts
    def prepare_game(self):
        for player in self.players:
            player.get_hand(self.hand_quantity)

    # determine the final winner
    def determine_winner(self):
        players = [player for player in self.players]
        winner = max(players, key=lambda x: x.stack)
        print("The winner: " + winner.name + ' with cards ' + str(winner.stack))
    # start the game loop
    def play(self):
        while self.round < self.hand_quantity:
            for player in self.players:
                player.drop()
            self.table.assign_to_winner()
            self.round += 1
        self.determine_winner()
