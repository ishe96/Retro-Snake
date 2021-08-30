import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.cursor_rect_rev = pygame.Rect(0, 0, 20, 20)
        self.offset = -100
        self.offset_rev = -120

    # Cursor
    def draw_cursor(self):
        self.game.draw_text('>', 25, self.cursor_rect.x, self.cursor_rect.y)
    
    def draw_cursor_rev(self):
        self.game.draw_text('<', 25, self.cursor_rect_rev.x, self.cursor_rect_rev.y)

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
        self.cursor_rect_rev.midtop = (self.startx - self.offset_rev, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('MENU', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_W / 2 -140)
            self.game.draw_text('Start Game', 20, self.startx, self.starty)
            self.game.draw_text("Game Play", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.game.draw_text("Exit", 20, self.endx, self.endy)
            self.draw_cursor()
            self.draw_cursor_rev()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.cursor_rect_rev.midtop = (self.optionsx - self.offset_rev, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.cursor_rect_rev.midtop = (self.creditsx - self.offset_rev, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.endx + self.offset, self.endy)
                self.cursor_rect_rev.midtop = (self.endx - self.offset_rev, self.endy)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.cursor_rect_rev.midtop = (self.startx - self.offset_rev, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.endx + self.offset, self.endy)
                self.cursor_rect_rev.midtop = (self.endx - self.offset_rev, self.endy)
                self.state = 'Exit'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.cursor_rect_rev.midtop = (self.startx - self.offset_rev, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.cursor_rect_rev.midtop = (self.optionsx - self.offset_rev, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.cursor_rect_rev.midtop = (self.creditsx - self.offset_rev, self.creditsy)
                self.state = 'Credits'
                
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.now_menu = self.game.options
            elif self.state == 'Credits':
                self.game.now_menu = self.game.credits
            elif self.state == 'Exit':
                self.game.now_menu = quit()
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Game Play', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -30)
            self.game.draw_text("Use Keyboard UP, DOWN, LEFT, RIGHT", 15, self.volx, self.voly)
            self.game.draw_text("to move snake.", 15, self.controlsx, self.controlsy)
            self.game.draw_text("UP ↑", 15, self.controlsx, self.controlsy + 20)
            self.game.draw_text("DOWN ↓", 15, self.controlsx, self.controlsy + 40)
            self.game.draw_text("LEFT ←", 15, self.controlsx, self.controlsy + 60)
            self.game.draw_text("RIGHT →", 15, self.controlsx, self.controlsy + 80)
            self.draw_cursor()
            self.draw_cursor_rev()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.now_menu = self.game.main_menu
            self.run_display = False
        elif self.game.START_KEY:
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.now_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -50)
            self.game.draw_text('Created by iSHE', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -20)
            self.blit_screen()