# Project setup

import pygame as pg
import random
from settings import *
from sprites import *


class Game:
    def __init__(self):
        # initilize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        self.clock.tick(FPS)
        self.events()
        self.update()
        self.draw()

    def update(self):
        # game Loop- update
        self.all_sprites.update()

    def events(self):
        # game Loop -events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                # check what is happaning here
                if self.playing:
                    self.playing = False
                self.playing = False

    def draw(self):
        # Game Loop -draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # "after" drawing everyting flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/ continue
        pass


g = Game()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
