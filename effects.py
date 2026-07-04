import pygame
from settings import WIDTH, HEIGHT

# ---------------- Explosion ---------------- #

class Explosion:

    def __init__(self):

        self.image = pygame.image.load(
            "assets/explosion.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (80, 80)
        )

        self.x = 0
        self.y = 0

        self.timer = 0

        self.active = False

    def start(self, x, y):

        self.x = x
        self.y = y

        self.timer = 25

        self.active = True

    def update(self):

        if self.active:

            self.timer -= 1

            if self.timer <= 0:
                self.active = False

    def draw(self, screen):

        if self.active:
            screen.blit(self.image, (self.x, self.y))


# ---------------- Screen Shake ---------------- #

class ScreenShake:

    def __init__(self):

        self.timer = 0
        self.strength = 0

    def start(self, strength=8, duration=15):

        self.strength = strength
        self.timer = duration

    def update(self):

        if self.timer > 0:
            self.timer -= 1

    def get_offset(self):

        if self.timer <= 0:
            return (0, 0)

        import random

        return (
            random.randint(-self.strength, self.strength),
            random.randint(-self.strength, self.strength)
        )


# ---------------- Boss Warning ---------------- #

class WarningBanner:

    def __init__(self):

        self.font = pygame.font.Font(
            "freesansbold.ttf",
            50
        )

        self.timer = 0

    def show(self):

        self.timer = 180

    def start(self):

        # Backward-compatible alias for existing game loop calls.
        self.show()

    def update(self):

        if self.timer > 0:
            self.timer -= 1

    def draw(self, screen):

        if self.timer > 0:

            text = self.font.render(
                "WARNING! BOSS INCOMING!",
                True,
                (255,0,0)
            )

            screen.blit(
                text,
                text.get_rect(center=(400,80))
            )


# ---------------- Damage Flash ---------------- #

class DamageFlash:

    def __init__(self):

        self.timer = 0

    def start(self):

        self.timer = 12

    def update(self):

        if self.timer > 0:
            self.timer -= 1

    def draw(self, screen):

        if self.timer > 0:

            overlay = pygame.Surface((WIDTH, HEIGHT))

            overlay.set_alpha(80)

            overlay.fill((255,0,0))

            screen.blit(overlay,(0,0))