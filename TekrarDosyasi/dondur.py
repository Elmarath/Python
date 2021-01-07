import pygame
from os import path

WIDTH = 480
HEIGH = 360
FPS = 60

GREEN = (0, 255, 0)
size = (WIDTH, HEIGH)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

pygame.init()
# load image
img_folder = path.join(path.dirname(__file__), 'img')
mobe_img = pygame.image.load(
    path.join(img_folder, 'playerShip2_red.png')).convert_alpha()


class Mobe(pygame.sprite.Sprite):
    # we create th mob here
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_org = mobe_img
        self.image = self.image_org.copy()
        self.rect = self.image.get_rect()
        self.rect.center = [200, 200]
        self.rot = 0
        self.rot_speed = 3

    # what the mob does goes here
    def update(self):
        self.rotate()

    def rotate(self):
        # donusturdugun resmi yazdir (yeni resim olacak)
        self.rot = (self.rot + self.rot_speed) % 360
        image_new = pygame.transform.rotate(self.image_org, self.rot)
        old_center = self.rect.center
        self.image = image_new
        # this part is important
        self.rect = image_new.get_rect()
        self.rect.center = old_center

        # donusturdugun resmin rect ini eski resimin center ina esitle


all_sprites = pygame.sprite.Group()
mobes = pygame.sprite.Group()

mobe = Mobe()
mobes.add(mobe)
all_sprites.add(mobes)

run = True
# make a while loop:
while run:
    # get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # update
    all_sprites.update()
    # render
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # waits for the gaps

pygame.quit()
