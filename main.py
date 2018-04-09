from cardgame.models import Card, Hand, Table, Player, Game

table = Table()
player1 = Player(table, name='Filip')
player2 = Player(table, name='Jan')

game = Game(table, [player1, player2], 5)
game.prepare_game()
game.play()
