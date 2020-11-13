import pygame
import random
import os

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")


class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        # idk what this do but required
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            os.path.join(img_folder, "MuscleDoge.png")).convert()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def update(self):
        self.speedx = 0
        keyState = pygame.key.get_pressed()
        if keyState[pygame.K_LEFT]:
            self.speedx = -5
        elif keyState[pygame.K_RIGHT]:
            self.speedx = +5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Mob(pygame.sprite.Sprite):
    # sprite for enemies
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = (os.path.join(img_folder, "YellingCad.png"), os.path.join(
            img_folder, "CryingCad.png"), os.path.join(img_folder, "BrokenCad.jpg"))
        self.RandImageIndex = random.randrange(0, 3)
        self.image = pygame.image.load(
            self.images[self.RandImageIndex]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.random()*6 - 3
        self.speedy = random.randrange(3, 8)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # if not in gameplay
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
            # spawn again
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(
            img_folder, "NoMuscleDoge.jpg")).convert()
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self. speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it reaches top of the screen
        if self.rect.bottom < 0:
            self.kill()
# refresh window


def redrawGameWindow():
    pygame.display.update()


# initialize pygame an create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MY Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(0, 16):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Game Loop
run = True
while run:
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closure
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            if event.key == pygame.K_ESCAPE:
                run = False
    # Update
    all_sprites.update()
    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    # check to see if a mob hit the player
    # returns: [<Mob sprite(in 2 groups)>, <Mob sprite(in 2 groups)>]
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        run = False
    # Draw / render
    screen.fill((210, 200, 210))
    all_sprites.draw(screen)

    redrawGameWindow()
