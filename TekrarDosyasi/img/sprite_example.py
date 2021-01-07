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


# Load all data
background = pygame.image.load(path.join(img_dir, 'space.png')).convert_alpha()
background_rect = background.get_rect()
player_img = pygame.image.load(
    path.join(img_dir, 'PlayerShip2_red.png')).convert_alpha()
meteor_img = pygame.image.load(path.join(
    img_dir, 'meteorBrown_big1.png')).convert_alpha()
laser_img = pygame.image.load(
    path.join(img_dir, 'laserRed16.png')).convert_alpha()
meteor_images = []
meteor_list = ['meteorBrown_big1.png', 'meteorGrey_big2.png',
               'meteorGrey_big3.png', 'meteorGrey_big4.png']


for img in meteor_list:
    meteor_images.append(pygame.image.load(
        path.join(img_dir, img)).convert_alpha())


class Player(pygame.sprite.Sprite):  # Player inherites from Sprite means player is a sprite
    def __init__(self):
        # sprite contrustor
        pygame.sprite.Sprite.__init__(self)
        # sprite image
        self.image = pygame.transform.scale(player_img, (50, 38))
        # sprite rect
        self.rect = self.image.get_rect()

        # first adjustments
        self.radius = 19  # we are overriting a radius value here so we can use this value in sprite.collide_circle
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
        self.image_org = random.choice(meteor_images)
        self.image_org = pygame.transform.scale(meteor_img, (45, 50))
        self.image = self.image_org.copy()  # we copied for the rotating function
        self.rect = self.image_org.get_rect()
        self.radius = 25
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH-self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        # last update holds the time difference between last called
        # get ticks has been since the game begun
        self.last_update = pygame.time.get_ticks()
        print(self.last_update)

    def rotate(self):
        now = pygame.time.get_ticks()  # now holds the time between since the game created
        # if the if block is true only than rotate the image
        if now - self.last_update > 50:  # if difference between now and the last update higher than 50 miliseconds
            self.last_update = now

            self.rot = (self.rot + self.rot_speed) % 360
            # we have to make a new image
            # we make a new image by returning the old image
            self.new_image = pygame.transform.rotate(
                self.image_org, self.rot)
            # we have to make a new rect.center because image turned but rect did not
            old_center = self.rect.center
            # self.image will be blited
            self.image = self.new_image
            # self.rect gets updated by the new image so it is resized
            self.rect = self.image.get_rect()
            # if we do not initilize the rect.center new rect's coords will be 0, 0
            self.rect.center = old_center

    def update(self):
        self.rotate()
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
    # check to see if a bullet hits a mob (ths one is between goups)
    hits = pygame.sprite.groupcollide(bullets, mobs, True, True)
    if hits:
        m = Mob()
        mobs.add(m)
        all_sprites.add(m)

    # check to see if a mob hits a player
    hits = pygame.sprite.spritecollide(
        player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        run = False

    # render
    screen.fill(BLACK)
    # blit copyies the image and paint the scene
    screen.blit(background, background_rect)
    all_sprites.draw(screen)  # all sprites had been drawn
    pygame.display.flip()  # display.flip makes everything redrawn once the loop at its end

pygame.quit()
