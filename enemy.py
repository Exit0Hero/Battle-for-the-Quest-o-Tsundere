import pygame
import random
from settings import *

class Enemy:

    def __init__(self):

        # Enemy Type
        self.type = random.randint(1, 3)

        if self.type == 1:
            image = "assets/enemy.webp"
            self.speed = NORMAL_SPEED

        elif self.type == 2:
            image = "assets/fast_enemy.png"
            self.speed = FAST_SPEED

        else:
            image = "assets/tank_enemy.png"
            self.speed = TANK_SPEED

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (ENEMY_WIDTH, ENEMY_HEIGHT)
        )

        self.reset()

    # -------------------------

    def update(self):

        self.move()

    # -------------------------

    def move(self):

        self.x += self.speed * self.direction

        if self.x <= 0:
            self.direction = 1
            self.y += ENEMY_DROP

        elif self.x >= WIDTH - ENEMY_WIDTH:
            self.direction = -1
            self.y += ENEMY_DROP

    # -------------------------

    def draw(self, screen):

        screen.blit(self.image, (self.x, self.y))

    # -------------------------

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            ENEMY_WIDTH,
            ENEMY_HEIGHT
        )

    # -------------------------

    def reset(self):

        self.x = random.randint(0, WIDTH - ENEMY_WIDTH)
        self.y = random.randint(40, 150)

        self.direction = random.choice([-1, 1])

        # Give a new random type each spawn
        self.type = random.randint(1, 3)

        if self.type == 1:
            image = "assets/enemy.webp"
            self.speed = NORMAL_SPEED

        elif self.type == 2:
            image = "assets/fast_enemy.png"
            self.speed = FAST_SPEED

        else:
            image = "assets/tank_enemy.png"
            self.speed = TANK_SPEED

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (ENEMY_WIDTH, ENEMY_HEIGHT)
        )
    def respawn(self):
        self.reset()