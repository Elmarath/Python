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

# set up assets folders
game_folder = os.path.dirname(__file__)
print(game_folder)
img_folder = os.path.join(game_folder, "images")


class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        # idk what this do but required
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

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
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(3, 8)

    def update(self):
        self.rect.y += self.speedy
        # if not in gameplay
        if self.rect.top > HEIGHT + 10:
            # spawn again
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 8)


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
player = Player()
all_sprites.add(player)
for i in range(0, 8):
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
    # Update
    all_sprites.update()
    #Draw / render
    screen.fill((210, 200, 210))
    all_sprites.draw(screen)

    redrawGameWindow()
