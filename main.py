"""
    Main module importing the necessary classes
    and implementing the 'startup screen'
"""
from cardgame.models import Card, Hand, Table, Player, Game

playerAmount = int(input('How many players? '))
deckSize = int(input('How many cards per deck? '))

players = []
table = Table()

for i in range(0, playerAmount):
    name = input('Enter name for Player ' + str(i+1) + ': ')
    players.append(Player(table, name=name))

game = Game(table, players, deckSize)
game.prepare_game()
game.play()
