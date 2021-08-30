import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    # Cursor
    def draw_cursor(self):
        self.game.draw_text('>', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

# Main Menu
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.endx, self.endy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('MENU', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_W / 2 -20)
            self.game.draw_text('Start Game', 20, self.startx, self.starty)
            self.game.draw_text('Options', 20, self.optionsx, self.optionsy)
            self.game.draw_text('Credits', 20, self.creditsx, self.creditsy)
            self.game.draw_text('Exit', 20, self.endx, self.endy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start Game':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.endx + self.offset, self.endy)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start Game'
        elif self.game.UP_KEY:
            if self.state == 'Start Game':
                self.cursor_rect.midtop = (self.endx + self.offset, self.endy)
                self.state = 'Exit'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start Game'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.start == 'Start Game':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.now_menu = self.game.options
            elif self.state == 'Credits':
                self.game.now_menu = self.game.credits
            elif self.state == 'Exit':
                quit()
            self.run_display = False

    def OptionsMenu(Menu):
        def __init__(self, game):
            Menu.__init__(self, game)
            self.state = 'How To Play'
            self.how_tox, self.how_toy = self.mid_w, self.mid_h + 20
            self.cursor_rect.midtop = (self.how_tox + self.offset, self.how_toy)

        def display_menu(self):
            self.run_display = True
            while self.run_display:
                self.game.check_events()
                self.check_input()
                self.game.display.fill((0, 0, 0))
                self.game.draw_text('How To Play', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -30)
                self.game.draw_text('Use keyboard arrows UP, DOWN, LEFT and RIGHt to move snake around the ground.', 15, self.how_tox, self.how_toy)
                self.draw_cursor()
                self.blit_screen()

        def check_input(self):
            if self.game.BACK_KEY:
                self.game.now_menu = self.game.main_menu
                self.run_display = False

    class CreditsMenu(Menu):
        def __init__(self, game):
            Menu.__init__(self, game)

        def display_menu(self):
            self.run_display = True
            while self.run_display:
                self.game.check_events()
                if self.game.START_KEY or self.game.BACK_KEY:
                    self.game.now_menu = self.game.main_menu
                    sel.run_display = False
                self.game.display.fill(self.game.BLACK)
                self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -20)
                self.game.draw_text('Created by iSHE', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -30)
                self.blit_screen()