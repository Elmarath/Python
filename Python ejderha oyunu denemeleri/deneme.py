from math import cos
import pygame
import math

pygame.init()

win = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("deneme")


def getAngle(main_x, main_y):
    mx, my = pygame.mouse.get_pos()
    egim = math.atan((my-main_y)/(mx-main_x))
    first_degrees = math.degrees(egim)
    last_degrees = 0
    if mx > main_x and my < main_y:  # birinci bolge
        last_degrees = first_degrees * (-1)
    elif mx < main_x and my < main_y:  # ikinci bolge
        last_degrees = 180 - first_degrees
    elif mx < main_x and my > main_y:  # ucuncu bolge
        last_degrees = first_degrees * (-1) + 180
    elif mx > main_x and my > main_y:  # dorduncu bolge
        last_degrees = 360 - first_degrees
    return last_degrees


main_x = 250
main_y = 250
vel = 3
x = 250
y = 250
bullets = []
run = True
# mainloop
while(run):
    clock.tick(5)
    angle = getAngle(main_x, main_y)
    x += math.cos(math.radians(angle)) * (vel)
    y += math.sin(math.radians(angle)) * (vel)
    pygame.draw.circle(win, (0, 255, 0), (int(x), int(y)), 10)

    pygame.draw.circle(win, (255, 0, 0), (main_x, main_y), 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
