import pygame
import random
from settings import *

class Boss:

    def __init__(self):

        self.image = pygame.image.load("assets/boss.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (BOSS_WIDTH, BOSS_HEIGHT)
        )

        self.x = WIDTH//2 - BOSS_WIDTH//2
        self.y = -250

        self.speed = BOSS_SPEED

        self.health = BOSS_HEALTH
        self.max_health = BOSS_HEALTH

        self.direction = 1

        self.active = False

        self.bullet_timer = 0

    # ----------------------------

    def spawn(self):

        self.active = True

        self.health = self.max_health

        self.x = WIDTH//2 - BOSS_WIDTH//2
        self.y = -250

        self.direction = 1

        self.bullet_timer = 0

    # ----------------------------

    def update(self):

        if not self.active:
            return

        if self.y < 40:
            self.y += 2
            return

        self.x += self.speed * self.direction

        if self.x <= 0:

            self.direction = 1

        elif self.x >= WIDTH - BOSS_WIDTH:

            self.direction = -1

        self.bullet_timer += 1

    # ----------------------------

    def draw(self, screen):

        if self.active:

            screen.blit(self.image,(self.x,self.y))

    # ----------------------------

    def damage(self):

        self.health -= 1

        if self.health <= 0:

            self.active = False

            return True

        return False

    # ----------------------------

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            BOSS_WIDTH,
            BOSS_HEIGHT
        )

    # ----------------------------

    def draw_health(self, screen):

        if not self.active:
            return

        pygame.draw.rect(
            screen,
            (100,100,100),
            (150,15,500,25)
        )

        width = int(
            500 * self.health / self.max_health
        )

        pygame.draw.rect(
            screen,
            (255,0,0),
            (150,15,width,25)
        )

class BossBullet:

    def __init__(self):

        self.active = False
        self.x = 0
        self.y = 0

        self.speed = 7

        self.image = pygame.Surface((12, 28))
        self.image.fill((255, 80, 80))

    def fire(self, x, y):

        self.active = True
        self.x = x
        self.y = y

    def update(self):

        if self.active:

            self.y += self.speed

            if self.y > HEIGHT:

                self.active = False

    def draw(self, screen):

        if self.active:
            screen.blit(self.image, (self.x, self.y))

    def get_rect(self):

        return pygame.Rect(self.x, self.y, 12, 28)

    def reset(self):

        self.active = False