# pygame template - skeleton for a new pygame project

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

run = True


# this takes the all sprites and makes easy to draw and update them
all_sprites = pygame.sprite.Group()

while run:
    # keep loop running at the right speed
    clock.tick(FPS)

    # process input (events)
    for event in pygame.event.get():  # pygame.event.get() holds the events that happened after the last time checked
        # check for closing window
        if event.type == pygame.QUIT:
            run = False

    # update
    all_sprites.update()  # all sprites updated
    all_sprites.draw(screen)  # all sprites had been drawn
    # render
    screen.fill(WHITE)
    pygame.display.flip()  # display.flip makes everything redrawn once the loop at its end

pygame.quit()
