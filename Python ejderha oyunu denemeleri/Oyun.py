import pygame
import math

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Dragon game")

background = pygame.image.load(
    'D:\Developing\Python\Python ejderha oyunu denemeleri\Images\Dungeon_Background.png')


def getAngle(paw_x, paw_y):
    mx, my = pygame.mouse.get_pos()

    if mx-paw_x == 0:
        mx = 0.0002
        paw_x = 0.0001
    slope = math.atan((my-paw_y)/(mx-paw_x))
    first_degrees = math.degrees(slope)
    print("oran: ", slope)
    print("ilk derece", first_degrees)
    last_degrees = 0
    if mx > paw_x and my < paw_y:  # birinci bolge
        last_degrees = first_degrees * (-1)
    elif mx < paw_x and my < paw_y:  # ikinci bolge
        last_degrees = 180 - first_degrees
    elif mx < paw_x and my > paw_y:  # ucuncu bolge
        last_degrees = first_degrees * (-1) + 180
    elif mx > paw_x and my > paw_y:  # dorduncu bolge
        last_degrees = 360 - first_degrees
    return last_degrees


class player(object):

    def __init__(self, x, y, width, height, vel, angle):
        self.player_image = pygame.image.load(
            'D:\Developing\Python\Python ejderha oyunu denemeleri\Images\BabyDragonImage.png')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.angle = angle

    # def rotate(self):
    #    self.player_image = pygame.transform.rotozoom(
    #        self.player_image, self.angle, 1)
    #    self.x = self.player_image.get_rect(center=(self.x, self.y)).x
    #    self.y = self.player_image.get_rect(center=(self.x, self.y)).y

    def rotate(self):
        rotated_surface = pygame.transform.rotozoom(
            self.player_image, self.angle, 1)
        rotated_rect = self.player_image.get_rect(
            center=(self.x + (self.width//2), self.y + (self.height//2)))
        return rotated_surface, rotated_rect.x, rotated_rect.y

    def draw(self, win, image, placex, placey):
        # self.player_image = pygame.transform.rotate(self.player_image, self.angle)
        # self.angle += 1 % 360
        win.blit(image, (placex -
                         (self.width/2), placey - (self.height/2)))
        pygame.draw.circle(
            win, (255, 0, 0), (self.x, self.y), 5)


class tiny_enemy(object):
    tiny_enemy_image = pygame.image.load(
        'D:\Developing\Python\Python ejderha oyunu denemeleri\Images\TinyEnemyImage.png')

    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def draw(self, win):
        win.blit(self.tiny_enemy_image,
                 (self.x-(self.width/2), self.y-(self.height/2)))
        pygame.draw.circle(
            win, (255, 0, 0), (self.x, self.y), 5)


class projectile(object):
    def __init__(self, x, y, radius, color, angle):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.angle = angle
        self.vel = 8


def createProjectile(bullets, angle):
    for bullet in bullets:
        if bullet.x < SCREEN_WIDTH and bullet.x > 0:
            bullet.x += math.cos(angle) * bullet.vel
        if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
            bullet.y += math.sin(angle) * bullet.vel


def redrawGameWindow():
    win.blit(background, (0, 0))
    dragon.draw(win, image, dragonx, dragony)
    tiny_knight.draw(win)

    pygame.display.update()


# mainloop
run = True
player_spawn_x = 350
player_spawn_y = 300
player_width = 64
player_height = 64
player_vel = 10
tiny_enemy_spawn_x = 400
tiny_enemy_spawn_y = 200
tiny_enemy_width = 64
tiny_enemy_height = 64
tiny_enemy_vel = 4
angle = 0

bullets = []

dragon = player(player_spawn_x, player_spawn_y,
                player_width, player_height, player_vel, angle)
tiny_knight = tiny_enemy(tiny_enemy_spawn_x, tiny_enemy_spawn_y,
                         tiny_enemy_width, tiny_enemy_height, tiny_enemy_vel)


while run:
    clock.tick(60)

    dragon.angle = getAngle(dragon.x, dragon.y)

    distance = pow((dragon.x - tiny_enemy_spawn_x)**2 +
                   (dragon.y - tiny_enemy_spawn_y)**2, 1/2)
    if distance < 300:
        if tiny_knight.x < dragon.x:
            tiny_knight.x += tiny_knight.vel
        if tiny_knight.x > dragon.x:
            tiny_knight.x -= tiny_knight.vel
        if tiny_knight.y < dragon.y:
            tiny_knight.y += tiny_knight.vel
        if tiny_knight.y > dragon.y:
            tiny_knight.y -= tiny_knight.vel

    # left button middle button right button
    M1, Mm, M2 = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    if M1 == True:
        if len(bullets) < 5:
            bullets.append(projectile(round(dragon.x + dragon.width // 2),
                                      round(dragon.y + dragon.height // 2), 6, (255, 0, 0), dragon.angle))
            createProjectile(bullets, dragon.angle)
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon.x > 0 + dragon.width//2:
        dragon.x -= dragon.vel
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon.x < SCREEN_WIDTH - dragon.width//2:
        dragon.x += dragon.vel
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon.y > 0 + dragon.height//2:
        dragon.y -= dragon.vel
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon.y < SCREEN_HEIGHT - dragon.height//2:
        dragon.y += dragon.vel
    if keys[pygame.K_ESCAPE]:
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    image, dragonx, dragony = dragon.rotate()

    redrawGameWindow()

pygame.quit()
