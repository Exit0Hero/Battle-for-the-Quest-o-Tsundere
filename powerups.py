import pygame
import random
from settings import *

# -------------------------------
# Power-up Types
# -------------------------------

LIFE = 1
SHIELD = 2
RAPID_FIRE = 3
BOMB = 4


class PowerUp:

    def __init__(self):

        self.active = False

        self.type = random.randint(1, 4)

        self.x = 0
        self.y = 0

        self.speed = POWERUP_SPEED

        self.load_image()

    def load_image(self):

        if self.type == LIFE:
            file = "assets/life.png"

        elif self.type == SHIELD:
            file = "assets/shield.png"

        elif self.type == RAPID_FIRE:
            file = "assets/rapidfire.png"

        else:
            file = "assets/bomb.png"

        self.image = pygame.image.load(file).convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (POWERUP_SIZE, POWERUP_SIZE)
        )

    def spawn(self, x, y):

        self.active = True

        self.x = x
        self.y = y

        self.type = random.randint(1, 4)

        self.load_image()

    def move(self):

        if self.active:

            self.y += self.speed

            if self.y > HEIGHT:
                self.active = False

    def draw(self, screen):

        if self.active:
            screen.blit(self.image, (self.x, self.y))

    def apply(self, player, enemies):

        if self.type == LIFE:

            player.heal()

        elif self.type == SHIELD:

            player.activate_shield()

        elif self.type == RAPID_FIRE:

            player.activate_rapid_fire()

        elif self.type == BOMB:

            for enemy in enemies:
                enemy.respawn()
                player.add_score(1)

        self.active = False

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            POWERUP_SIZE,
            POWERUP_SIZE
        )