import pygame
import time

pygame.init()

x_max = 680
y_max = 680

win = pygame.display.set_mode((x_max, y_max))

pygame.display.set_caption("First Game")

x = 230
y = 220
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < x_max-width-vel:
        x += vel
    if keys[pygame.K_UP] and y >vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < y_max-height-vel:
        y += vel


    win.fill((0, 0, 0))
    pygame.draw.rect(win,(100, 0, 255), (x, y, width, height))
    pygame.display.update()




pygame.quit()