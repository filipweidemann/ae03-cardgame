import pytest
from cardgame.models import Game, Player, Table, Hand, Card

@pytest.fixture(scope='function')
def game():
    deckSize = 5
    table1 = Table()
    player1 = Player(table1, 'Player1')
    player2 = Player(table1, 'Player2')
    return Game(table1, [player1, player2], deckSize)


def test_deck_size(game):
    game.prepare_game()
    assert len(game.players[0].hand.cards) == 5
    assert len(game.players[1].hand.cards) == 5

def test_card_winner(game):
    game.prepare_game()
    game.table.add_card((Card(5).value, game.players[0]))
    game.table.add_card((Card(4).value, game.players[1]))
    game.table.assign_to_winner()
    assert len(game.players[0].stack) == 2

def test_draw(game):
    game.prepare_game()
    game.table.add_card((Card(5).value, game.players[0]))
    game.table.add_card((Card(5).value, game.players[1]))
    game.table.assign_to_winner()
    assert len(game.players[0].stack) == 0
    assert len(game.players[1].stack) == 0
