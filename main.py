from sngame import *

g = Game()

while g.running:
    g.now_menu.display_menu()
    g.snk_game_loop()