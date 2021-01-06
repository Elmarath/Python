# shmup game
from os import path
import pygame
import random

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initiliaze pygame and create window
pygame.init()  # pygame starts
pygame.mixer.init()  # mixer handles the all the sound effects in the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):  # Player inherites from Sprite means player is a sprite
    def __init__(self):
        # sprite contrustor
        pygame.sprite.Sprite.__init__(self)
        # sprite image
        self.image = pygame.transform.scale(player_img, (50, 38))
        # sprite rect
        self.rect = self.image.get_rect()

        # first adjustments
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT - 35
        self.speedx = 0

    def update(self):
        self.speedx = 0
        # initializing the speedx
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        # initializing the rect position
        self.rect.centerx += self.speedx

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(meteor_img, (45, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH-self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH-self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


# Load all data
background = pygame.image.load(path.join(img_dir, 'space.png')).convert_alpha()
background_rect = background.get_rect()
player_img = pygame.image.load(
    path.join(img_dir, 'PlayerShip2_red.png')).convert_alpha()
meteor_img = pygame.image.load(path.join(
    img_dir, 'meteorBrown_big1.png')).convert_alpha()
laser_img = pygame.image.load(
    path.join(img_dir, 'laserRed16.png')).convert_alpha()

# this takes the all sprites and makes easy to draw and update them
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(0, 8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

run = True

while run:
    # keep loop running at the right speed
    clock.tick(FPS)

    # process input (events)
    for event in pygame.event.get():  # pygame.event.get() holds the events that happened after the last time checked
        # check for closing window
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # update
    all_sprites.update()  # all sprites updated
    player.update()
    # check to see if a bullet hits a mob (ths one is between goups)
    hits = pygame.sprite.groupcollide(bullets, mobs, True, True)
    if hits:
        m = Mob()
        mobs.add(m)
        all_sprites.add(m)

    # check to see if a mob hits a player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        run = False

    # render
    screen.fill(BLACK)
    # blit copyies the image and paint the scene
    screen.blit(background, background_rect)
    all_sprites.draw(screen)  # all sprites had been drawn
    pygame.display.flip()  # display.flip makes everything redrawn once the loop at its end

pygame.quit()
