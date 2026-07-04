import pygame
from settings import *

class UI:

    def __init__(self):

        self.small = pygame.font.SysFont("verdana", 24)
        self.medium = pygame.font.SysFont("georgia", 38, bold=True)
        self.large = pygame.font.SysFont("impact", 66)

    # -------------------------
    # Score
    # -------------------------

    def draw_score(self, screen, score, high_score=0):

        score_text = self.small.render(
            f"Score : {score}",
            True,
            WHITE
        )

        high_text = self.small.render(
            f"High : {high_score}",
            True,
            YELLOW
        )

        screen.blit(score_text, (10, 10))
        screen.blit(high_text, (10, 45))

    # -------------------------
    # Lives
    # -------------------------

    def draw_lives(self, screen, lives):

        text = self.small.render(
            f"Lives : {lives}",
            True,
            RED
        )

        screen.blit(text, (650, 10))

    # -------------------------
    # Level
    # -------------------------

    def draw_level(self, screen, level):

        text = self.small.render(
            f"Level : {level}",
            True,
            GREEN
        )

        screen.blit(text, (330, 10))

    # -------------------------
    # Menu
    # -------------------------

    def draw_menu(self, screen):

        title_top = self.large.render(
            "BATTLE FOR THE QUEST",
            True,
            WHITE
        )

        title_bottom = self.large.render(
            "OF TSUNDERE",
            True,
            WHITE
        )

        start = self.medium.render(
            "Press SPACE to Start",
            True,
            YELLOW
        )

        hint = self.small.render(
            "Move: LEFT/RIGHT   Pause: P",
            True,
            WHITE
        )

        center_x = WIDTH // 2

        screen.blit(title_top, title_top.get_rect(center=(center_x, 135)))
        screen.blit(title_bottom, title_bottom.get_rect(center=(center_x, 205)))
        screen.blit(start, start.get_rect(center=(center_x, 320)))
        screen.blit(hint, hint.get_rect(center=(center_x, 380)))


    def draw_highscore(self, screen, high_score):

        text = self.small.render(
            f"High Score : {high_score}",
            True,
            YELLOW
        )

        screen.blit(text, (10, 45))

    # -------------------------
    # Pause
    # -------------------------

    def draw_pause(self, screen):

        title = self.large.render(
            "PAUSED",
            True,
            WHITE
        )

        resume = self.medium.render(
            "Press P to Continue",
            True,
            YELLOW
        )

        screen.blit(title, title.get_rect(center=(400,220)))
        screen.blit(resume, resume.get_rect(center=(400,320)))

    # -------------------------
    # Game Over
    # -------------------------

    def draw_game_over(self, screen, score, high):

        title = self.large.render(
            "GAME OVER",
            True,
            RED
        )

        final = self.medium.render(
            f"Score : {score}",
            True,
            WHITE
        )

        best = self.medium.render(
            f"High Score : {high}",
            True,
            YELLOW
        )

        restart = self.medium.render(
            "Press R to Restart",
            True,
            GREEN
        )

        quit_text = self.small.render(
            "Press ESC to Quit",
            True,
            WHITE
        )

        screen.blit(title, title.get_rect(center=(400,140)))
        screen.blit(final, final.get_rect(center=(400,250)))
        screen.blit(best, best.get_rect(center=(400,300)))
        screen.blit(restart, restart.get_rect(center=(400,430)))
        screen.blit(quit_text, quit_text.get_rect(center=(400,480)))

    # -------------------------
    # Victory
    # -------------------------

    def draw_victory(self, screen, score):

        title = self.large.render(
            "YOU WIN!",
            True,
            GREEN
        )

        score_text = self.medium.render(
            f"Final Score : {score}",
            True,
            WHITE
        )

        restart = self.medium.render(
            "Press R to Play Again",
            True,
            YELLOW
        )

        screen.blit(title, title.get_rect(center=(400,200)))
        screen.blit(score_text, score_text.get_rect(center=(400,300)))
        screen.blit(restart, restart.get_rect(center=(400,410)))

    # -------------------------
    # FPS
    # -------------------------
    def draw_fps(self, screen, fps):

        text = self.small.render(
            f"FPS : {fps}",
            True,
            GREEN
        )

        screen.blit(text, (690, 45))