# pygame template - skeleton for a new pygame project
from os import path
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

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
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

# load data
img_folder = path.join(path.dirname(__file__), 'img')
player_img = pygame.image.load(path.join(img_folder, 'playerShip2_red.png'))
mob_img = pygame.image.load(path.join(img_folder, 'meteorBrown_big1.png'))
bullet_img = pygame.image.load(path.join(img_folder, 'laserRed16.png'))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image = pygame.transform.scale(self.image, (34, 34))
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT - 50
        self.rect.centerx = WIDTH / 2
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx -= 8
        if keystate[pygame.K_RIGHT]:
            self.speedx += 8

        self.rect.centerx = self.rect.centerx + self.speedx

    def shoot(self):
        print("shoot")
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        bullets.add(bullet)
        all_sprites.add(bullets)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image = pygame.transform.scale(self.image, (6, 30))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.speedy = -10

    def update(self):
        self.rect.centery = self.rect.centery + self.speedy
        if(self.rect.centery < -30):
            self.kill()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob_img
        self.image_org = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.centery = -50
        self.rect.centerx = random.randrange(-10, WIDTH)
        self.speedy = random.randrange(2, 8)
        self.rot = 0
        self.rot_speed = 10

    def update(self):
        self.rotate()
        self.rect.centery = self.rect.centery + self.speedy
        if (self.rect.topleft[1] > HEIGHT):
            self.kill()
            # create mob 
            
            m = Mob()
            mobs.add(m)
            all_sprites.add(mobs)

    def rotate(self):
        self.rot = (self.rot + self.rot_speed) % 360
        image_new = pygame.transform.rotate(self.image_org, self.rot)
        old_center = self.rect.center
        self.image = image_new
        # this part is important
        self.rect = image_new.get_rect()
        self.rect.center = old_center


# this takes the all sprites and makes easy to draw and update them
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()

for i in range(5):
    m = Mob()
    mobs.add(m)

all_sprites.add(player)
all_sprites.add(mobs)
all_sprites.add(bullets)

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
    hits = pygame.sprite.spritecollide(player, mobs, True)
    if hits:
        run = False

    hits = pygame.sprite.groupcollide(bullets, mobs, True, True)
    for hit in range(len(hits)):
        m = Mob()
        mobs.add(m)
        all_sprites.add(mobs)

    # render
    screen.fill(WHITE)
    all_sprites.draw(screen)  # all sprites had been drawn
    pygame.display.flip()  # display.flip makes everything redrawn once the loop at its end

pygame.quit()
