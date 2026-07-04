import pygame
from settings import *

class Bullet:

    def __init__(self):

        self.image = pygame.image.load(
            "assets/food.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (64, 64)
        )

        self.x = 0
        self.y = PLAYER_START_Y

        self.speed = PLAYER_BULLET_SPEED
        self.ready = True
        self.active = False

    # -------------------------
    # Fire Bullet
    # -------------------------

    def fire(self, x, y):

        if self.ready:
            self.ready = False
            self.active = True
            self.x = x
            self.y = y

    # -------------------------
    # Update
    # -------------------------

    def update(self):

        if self.active:

            self.y -= self.speed

            if self.y < -50:
                self.reset()

    # -------------------------
    # Draw
    # -------------------------

    def draw(self, screen):

        if self.active:
            screen.blit(self.image, (self.x + 16, self.y + 10))

    # -------------------------
    # Rectangle
    # -------------------------

    def get_rect(self):

        return pygame.Rect(
            self.x + 16,
            self.y + 10,
            32,
            32
        )

    # -------------------------
    # Reset
    # -------------------------

    def reset(self):

        self.active = False
        self.ready = True
        self.x = 0
        self.y = PLAYER_START_Y
# ==========================================
# Enemy Bullet
# ==========================================

class EnemyBullet:

    def __init__(self):

        self.image = pygame.Surface((12, 28))
        self.image.fill((255, 60, 60))

        self.x = 0
        self.y = 0

        self.speed = ENEMY_BULLET_SPEED

        self.active = False

    def fire(self, x, y):

        if not self.active:
            self.active = True
            self.x = x
            self.y = y

    def update(self):

        if self.active:

            self.y += self.speed

            if self.y > HEIGHT:
                self.reset()

    def draw(self, screen):

        if self.active:
            screen.blit(self.image, (self.x, self.y))

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            12,
            28
        )

    def reset(self):

        self.active = False