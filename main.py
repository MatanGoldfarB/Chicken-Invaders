import pygame
from classes import Player, Bullet, Enemy, EnemyBullet
import math
from pygame import mixer
level_1 = False
level_2 = False
level_3 = False
level_4 = False
level_5 = False
level_6 = False
level_7 = False
level_8 = False
level_9 = False
level_10 = False
# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background.png")
start_screen = pygame.image.load("start-screen.png")
# background sound
# mixer.music.load("directory.wav")
# mixer.music.play(-1)
# Title and Icon
pygame.display.set_caption("Chicken Invaders")
icon = pygame.image.load("chicken.png")
pygame.display.set_icon(icon)

font = pygame.font.Font('freesansbold.ttf', 100)


def show_game_over(x, y):
    score = font.render("Game Over", True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_level(x, y, level):
    score = font.render("Level " + str(level), True, (255, 255, 255))
    screen.blit(score, (x, y))


def isCollision(enemy, bullet, num):
    distance = math.sqrt(math.pow(enemy.x - bullet.x, 2) + math.pow(enemy.y - bullet.y, 2))

    if distance < num:
        return True
    return False


player = Player()
bullets = []
enemies = []
enemy_bullet = []
enemyX, enemyY = 80, 60
for i in range(1, 41):
    enemies.append(Enemy(enemyX, enemyY, 1))
    if i % 10 == 0:
        enemyY += 70
        enemyX = 80
    else:
        enemyX += 70

enemy_direction = True

# starting screen
first_screen = True
while first_screen:
    # RGB - RED, GREEN, BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    screen.blit(start_screen, (250, 150))
    # Until we quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            first_screen = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseX, mouseY = pygame.mouse.get_pos()
                if 250 < mouseX < 535 and 325 < mouseY < 370:
                    first_screen = False
                    between = True

    pygame.display.update()

# between scenes
count = 0
while between:
    # RGB - RED, GREEN, BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            between = False

    show_level(220, 150, 1)
    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    player.set_place(x, y)
    player.display_player(screen)

    pygame.display.update()
    count += 1
    if count == 250:
        level_1 = True
        break

# level 1
while level_1:

    # RGB - RED, GREEN, BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    # Until we quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            level_1 = False
            between = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.fire_state >= 25:
                player.fire_state = 0
                bullets.append(Bullet(player.x, player.y))

    # displaying all bullets
    for bullet in bullets:
        bullet.display_bullet(screen)
        bullet.y += bullet.y_change
        if bullet.y <= -50:
            bullets.remove(bullet)

    for bullet in bullets:
        for enemy in enemies:
            if isCollision(enemy, bullet, 25):
                if enemy.life == 1:
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    hit = mixer.Sound("chickenhit.wav")
                    hit.play()
                    continue
                else:
                    bullets.remove(bullet)
                    enemy.get_shot()
                    continue

    # display all enemies
    for enemy in enemies:
        enemy.display_enemy(screen)
        if isCollision(enemy, player, 50):
            level_1 = False
            between = False
            game_over = True
        if enemy.fire_state == 1000:
            enemy.fire_state = 0
            enemy_bullet.append(EnemyBullet(enemy.x, enemy.y))
        else:
            enemy.fire_state += 0.5
        if enemy_direction:
            enemy.x += 0.5
            if enemy.x >= 760:
                enemy_direction = False
        else:
            if enemy.x <= 50:
                enemy_direction = True
            enemy.x -= 0.5

    # display chicken eggs
    for bullet in enemy_bullet:
        bullet.display_bullet(screen)
        if isCollision(bullet, player, 50):
            level_1 = False
            between = False
            game_over = True
        bullet.y += bullet.y_change
        if bullet.y >= 800:
            enemy_bullet.remove(bullet)

    # displaying player
    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    player.set_place(x, y)
    player.display_player(screen)
    player.fire_state += 1

    if len(enemies) == 0:
        level_2 = True
        level_1 = False
    pygame.display.update()

# setting up level 2
if level_2:
    bullets = []
    enemies = []
    enemy_bullet = []
    enemyX, enemyY = 80, 60
    for i in range(1, 41):
        enemies.append(Enemy(enemyX, enemyY, 2))
        if i % 10 == 0:
            enemyY += 70
            enemyX = 80
        else:
            enemyX += 70

# between levels
count = 0
while between:
    # RGB - RED, GREEN, BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            between = False

    show_level(220, 150, 2)
    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    player.set_place(x, y)
    player.display_player(screen)

    pygame.display.update()
    count += 1
    if count == 250:
        break

# level 2
while level_2:

    # RGB - RED, GREEN, BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    # Until we quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            level_2 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.fire_state >= 25:
                player.fire_state = 0
                bullets.append(Bullet(player.x, player.y))

    # displaying all bullets
    for bullet in bullets:
        bullet.display_bullet(screen)
        bullet.y += bullet.y_change
        if bullet.y <= -50:
            bullets.remove(bullet)

    for bullet in bullets:
        for enemy in enemies:
            if isCollision(enemy, bullet, 25):
                if enemy.life == 1:
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    hit = pygame.mixer.Sound("chickenhit.wav")
                    hit.play()
                    continue
                else:
                    bullets.remove(bullet)
                    enemy.get_shot()
                    continue

    # display all enemies
    for enemy in enemies:
        enemy.display_enemy(screen)
        if isCollision(enemy, player, 50):
            level_2 = False
            game_over = True
        if enemy.fire_state == 1000:
            enemy.fire_state = 0
            enemy_bullet.append(EnemyBullet(enemy.x, enemy.y))
        else:
            enemy.fire_state += 0.5
        if enemy_direction:
            enemy.x += 0.5
            if enemy.x >= 760:
                enemy_direction = False
        else:
            if enemy.x <= 50:
                enemy_direction = True
            enemy.x -= 0.5

    # display chicken eggs
    for bullet in enemy_bullet:
        bullet.display_bullet(screen)
        if isCollision(bullet, player, 50):
            level_2 = False
            game_over = True
        bullet.y += bullet.y_change
        if bullet.y >= 800:
            enemy_bullet.remove(bullet)

    # displaying player
    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    player.set_place(x, y)
    player.display_player(screen)
    player.fire_state += 1

    if len(enemies) == 0:
        level_3 = True
        level_2 = False
    pygame.display.update()

# setting up level 3
if level_3:
    bullets = []
    enemies = []
    enemy_bullet = []
    enemyX, enemyY = 80, 60
    for i in range(1, 41):
        enemies.append(Enemy(enemyX, enemyY, 3))
        if i % 10 == 0:
            enemyY += 70
            enemyX = 80
        else:
            enemyX += 70

# between levels
count = 0
while between:
    # RGB - RED, GREEN, BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            between = False

    show_level(220, 150, 3)
    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    player.set_place(x, y)
    player.display_player(screen)

    pygame.display.update()
    count += 1
    if count == 250:
        break

# level 3
while level_3:

    # RGB - RED, GREEN, BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    # Until we quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            level_3 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.fire_state >= 25:
                player.fire_state = 0
                bullets.append(Bullet(player.x, player.y))

    # displaying all bullets
    for bullet in bullets:
        bullet.display_bullet(screen)
        bullet.y += bullet.y_change
        if bullet.y <= -50:
            bullets.remove(bullet)

    for bullet in bullets:
        for enemy in enemies:
            if isCollision(enemy, bullet, 25):
                if enemy.life == 1:
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    hit = pygame.mixer.Sound("chickenhit.wav")
                    hit.play()
                    continue
                else:
                    bullets.remove(bullet)
                    enemy.get_shot()
                    continue

    # display all enemies
    for enemy in enemies:
        enemy.display_enemy(screen)
        if isCollision(enemy, player, 50):
            level_3 = False
            game_over = True
        if enemy.fire_state == 1000:
            enemy.fire_state = 0
            enemy_bullet.append(EnemyBullet(enemy.x, enemy.y))
        else:
            enemy.fire_state += 0.5
        if enemy_direction:
            enemy.x += 0.5
            if enemy.x >= 760:
                enemy_direction = False
        else:
            if enemy.x <= 50:
                enemy_direction = True
            enemy.x -= 0.5

    # display chicken eggs
    for bullet in enemy_bullet:
        bullet.display_bullet(screen)
        if isCollision(bullet, player, 50):
            level_3 = False
            game_over = True
        bullet.y += bullet.y_change
        if bullet.y >= 800:
            enemy_bullet.remove(bullet)

    # displaying player
    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    player.set_place(x, y)
    player.display_player(screen)
    player.fire_state += 1

    if len(enemies) == 0:
        level_4 = True
        level_3 = False
    pygame.display.update()

# game over screen
while game_over:
    # RGB - RED, GREEN, BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

    show_game_over(110, 150)
    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    player.set_place(x, y)
    player.display_player(screen)

    pygame.display.update()