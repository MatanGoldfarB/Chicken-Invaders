import pygame
import random


class Player:
    def __init__(self):
        self.x = 340
        self.y = 480
        self.fire_state = 25
        self.img = pygame.image.load("rocket.png")

    def set_place(self, x, y):
        self.x = x
        self.y = y

    def display_player(self, screen):
        screen.blit(self.img, (self.x - 50, self.y - 50))


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_change = -5
        self.img = pygame.image.load("bullet.png")

    def display_bullet(self, screen):
        screen.blit(self.img, (self.x - 10, self.y))


class Enemy:
    def __init__(self, x, y, life):
        self.y = y
        self.x = x
        self.life = life
        self.fire_state = random.randint(0, 950)
        self.img = pygame.image.load(f"enemy{life}.png")

    def display_enemy(self, screen):
        screen.blit(self.img, (self.x - 32, self.y - 32))

    def get_shot(self):
        self.life -= 1
        self.img = pygame.image.load(f"enemy{self.life}.png")
        hit = pygame.mixer.Sound("chickenhit.wav")
        hit.play()

class EnemyBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_change = 1
        self.img = pygame.image.load("egg.png")

    def display_bullet(self, screen):
        screen.blit(self.img, (self.x - 16, self.y - 16))
