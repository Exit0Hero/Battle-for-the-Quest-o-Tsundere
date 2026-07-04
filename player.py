import pygame
from settings import *

class Player:

    def __init__(self):

        self.image = pygame.image.load(
            "assets/hero.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        )

        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y

        self.speed = PLAYER_SPEED

        self.lives = PLAYER_LIVES
        self.score = 0

        # movement flags
        self.move_left = False
        self.move_right = False

        # powerups
        self.rapid_fire = False
        self.rapid_fire_timer = 0
        self.shield_active = False
        self.shield_timer = 0

    # -------------------------

    def update(self):

        if self.move_left:
            self.x -= self.speed

        if self.move_right:
            self.x += self.speed

        # keep inside screen
        if self.x < 0:
            self.x = 0

        if self.x > WIDTH - PLAYER_WIDTH:
            self.x = WIDTH - PLAYER_WIDTH

        if self.rapid_fire_timer > 0:
            self.rapid_fire_timer -= 1
        else:
            self.rapid_fire = False

        if self.shield_timer > 0:
            self.shield_timer -= 1
        else:
            self.shield_active = False

    # -------------------------

    def draw(self, screen):

        screen.blit(self.image, (self.x, self.y))

        if self.shield_active:
            # Light shield ring to make temporary invulnerability readable.
            center = (
                int(self.x + PLAYER_WIDTH // 2),
                int(self.y + PLAYER_HEIGHT // 2)
            )
            pygame.draw.circle(screen, BLUE, center, 58, 3)

    # -------------------------

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            PLAYER_WIDTH,
            PLAYER_HEIGHT
        )

    # -------------------------

    def hit(self):

        if self.shield_active:
            return

        self.lives -= 1

    # -------------------------

    def add_score(self, points):

        self.score += points

    # -------------------------

    def reset(self):

        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y

        self.move_left = False
        self.move_right = False

        self.lives = PLAYER_LIVES
        self.score = 0
        self.rapid_fire = False
        self.rapid_fire_timer = 0
        self.shield_active = False
        self.shield_timer = 0

    # -------------------------

    def heal(self):

        self.lives += 1

    # -------------------------

    def activate_shield(self, duration_frames=FPS * 4):

        self.shield_active = True
        self.shield_timer = duration_frames

    # -------------------------

    def activate_rapid_fire(self, duration_frames=FPS * 5):

        self.rapid_fire = True
        self.rapid_fire_timer = duration_frames