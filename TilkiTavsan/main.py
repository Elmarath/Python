import pygame as pg
import sys
from os import path
from settings import*
from sprites import*
from tilemap import*


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'level.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect() = self.map_img.get_rect()
        self.rabbit_img = pg.image.load(
            path.join(img_folder, RABBIT_IMG)).convert_alpha()
        self.fox_img = pg.image.load(
            path.join(img_folder, FOX_IMG)).convert_alpha()
    
    def run(self):
        # game loop - set self.playing = false to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000.0 
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sorites.update()
    
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.blit(self.map_img)

    for sprite in self.all_sprites:
        if isinstance(spi)


while True:
    pass
