import pygame


def bullet_hits_enemy(bullet, enemy):

    if not bullet.active:
        return False

    bullet_rect = pygame.Rect(
        bullet.x,
        bullet.y,
        bullet.image.get_width(),
        bullet.image.get_height()
    )

    enemy_rect = pygame.Rect(
        enemy.x,
        enemy.y,
        enemy.image.get_width(),
        enemy.image.get_height()
    )

    return bullet_rect.colliderect(enemy_rect)


def enemy_bullet_hits_player(enemy_bullet, player):

    if not enemy_bullet.active:
        return False

    bullet_rect = pygame.Rect(
        enemy_bullet.x,
        enemy_bullet.y,
        enemy_bullet.image.get_width(),
        enemy_bullet.image.get_height()
    )

    return bullet_rect.colliderect(player.get_rect())


def enemy_hits_player(enemy, player):

    enemy_rect = pygame.Rect(
        enemy.x,
        enemy.y,
        enemy.image.get_width(),
        enemy.image.get_height()
    )

    return enemy_rect.colliderect(player.get_rect())


def boss_hits_player(boss, player):

    boss_rect = pygame.Rect(
        boss.x,
        boss.y,
        boss.image.get_width(),
        boss.image.get_height()
    )

    return boss_rect.colliderect(player.get_rect())


def powerup_collected(powerup, player):

    power_rect = pygame.Rect(
        powerup.x,
        powerup.y,
        powerup.image.get_width(),
        powerup.image.get_height()
    )

    return power_rect.colliderect(player.get_rect())