import pygame
import math

pygame.init()

win = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("deneme")

main_x = 250
main_y = 250
run = True
# mainloop
while(run):
    clock.tick(5)

    print("atan(1)", math.degrees(math.atan(1)))
    mx, my = pygame.mouse.get_pos()

    egim = math.atan((my-main_y)/(mx-main_x))
    first_degrees = math.degrees(egim)
    print("oran: ", egim)
    print("ilk derece", first_degrees)
    last_degrees = 0
    if mx > main_x and my < main_y:  # birinci bolge
        last_degrees = first_degrees * (-1)
    elif mx < main_x and my < main_y:  # ikinci bolge
        last_degrees = 180 - first_degrees
    elif mx < main_x and my > main_y:  # ucuncu bolge
        last_degrees = first_degrees * (-1) + 180
    elif mx > main_x and my > main_y:  # dorduncu bolge
        last_degrees = 360 - first_degrees

    print("son derece: ", last_degrees)

    pygame.draw.circle(win, (255, 0, 0), (main_x, main_y), 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
