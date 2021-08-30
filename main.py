from sngame import Game

g = Game()

while g.running:
    g.now_menu.display_menu()
    g.game_loop()