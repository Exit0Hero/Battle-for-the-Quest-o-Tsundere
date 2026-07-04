import pygame
import random
from pygame import mixer

from settings import *
from player import Player
from enemy import Enemy
from bullet import Bullet, EnemyBullet
from boss import Boss, BossBullet
from powerups import PowerUp
from collision import *
from effects import *
from ui import UI
from save import *

pygame.init()
mixer.init()

# ---------------------------
# Screen
# ---------------------------

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle for the quest of Tsundere")

clock = pygame.time.Clock()

# ---------------------------
# Assets
# ---------------------------

background = pygame.image.load(
    "assets/background.png"
).convert()

background = pygame.transform.scale(
    background,
    (WIDTH, HEIGHT)
)

icon = pygame.image.load(
    "assets/icon.png"
).convert_alpha()

pygame.display.set_icon(icon)

# ---------------------------
# Music
# ---------------------------

mixer.music.load("assets/reze.wav")
mixer.music.play(-1)

laser_sound = mixer.Sound("assets/laser.wav")
explosion_sound = mixer.Sound("assets/explosion.wav")

# ---------------------------
# Save
# ---------------------------

high_score = load_highscore()

# ---------------------------
# UI
# ---------------------------

ui = UI()

# ---------------------------
# Player
# ---------------------------

player = Player()

# ---------------------------
# Bullet
# ---------------------------

bullet = Bullet()

# ---------------------------
# Enemies
# ---------------------------

enemies = []

for i in range(NUM_ENEMIES):

    enemies.append(Enemy())

# ---------------------------
# Enemy Bullets
# ---------------------------

enemy_bullets = []

for i in range(NUM_ENEMIES):

    enemy_bullets.append(EnemyBullet())

# ---------------------------
# Boss
# ---------------------------

boss = Boss()

boss_bullets = []

for i in range(12):

    boss_bullets.append(BossBullet())

# ---------------------------
# Powerups
# ---------------------------

powerup = PowerUp()

# ---------------------------
# Effects
# ---------------------------

explosion = Explosion()

screen_shake = ScreenShake()

warning = WarningBanner()

damage_flash = DamageFlash()

# ---------------------------
# Game Variables
# ---------------------------

game_state = "menu"

running = True

level = 1

boss_spawned = False

rapid_fire_timer = 0

shoot_delay = 15

shoot_timer = 0

victory = False

fire_button_held = False


def restart_game():

    global player, bullet, enemies, enemy_bullets
    global boss, boss_bullets, powerup
    global explosion, screen_shake, warning, damage_flash
    global level, boss_spawned, rapid_fire_timer, shoot_timer
    global fire_button_held, game_state

    player = Player()
    bullet = Bullet()

    enemies = [Enemy() for _ in range(NUM_ENEMIES)]
    enemy_bullets = [EnemyBullet() for _ in range(NUM_ENEMIES)]

    boss = Boss()
    boss_bullets = [BossBullet() for _ in range(12)]

    powerup = PowerUp()

    explosion = Explosion()
    screen_shake = ScreenShake()
    warning = WarningBanner()
    damage_flash = DamageFlash()

    level = 1
    boss_spawned = False
    rapid_fire_timer = 0
    shoot_timer = 0
    fire_button_held = False
    game_state = "playing"


# -----------------------------------
# MAIN GAME LOOP
# -----------------------------------

while running:

    clock.tick(FPS)

    # Background
    screen.blit(background, (0, 0))

    # -----------------------------------
    # EVENTS
    # -----------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # ---------------- MENU ----------------

            if game_state == "menu":

                if event.key == pygame.K_SPACE:

                    game_state = "playing"

                elif event.key == pygame.K_ESCAPE:

                    running = False

            # ---------------- PLAYING ----------------

            elif game_state == "playing":

                if event.key == pygame.K_LEFT:

                    player.move_left = True

                elif event.key == pygame.K_RIGHT:

                    player.move_right = True

                elif event.key == pygame.K_SPACE:
                    fire_button_held = True

                elif event.key == pygame.K_p:

                    game_state = "paused"

            # ---------------- PAUSED ----------------

            elif game_state == "paused":

                if event.key == pygame.K_p:

                    game_state = "playing"

            # ---------------- GAME OVER ----------------

            elif game_state == "game_over":

                if event.key == pygame.K_r:

                    restart_game()

                elif event.key == pygame.K_ESCAPE:

                    running = False

            # ---------------- VICTORY ----------------

            elif game_state == "victory":

                if event.key == pygame.K_r:

                    restart_game()

                elif event.key == pygame.K_ESCAPE:

                    running = False

        # ---------------- KEY RELEASE ----------------

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:

                player.move_left = False

            elif event.key == pygame.K_RIGHT:

                player.move_right = False

            elif event.key == pygame.K_SPACE:

                fire_button_held = False


    # -----------------------------------
    # GAME STATES
    # -----------------------------------

    if game_state == "menu":

        ui.draw_menu(screen)

        pygame.display.update()

        continue


    if game_state == "paused":

        ui.draw_pause(screen)

        pygame.display.update()

        continue


    if game_state == "game_over":

        ui.draw_game_over(
            screen,
            player.score,
            high_score
        )

        pygame.display.update()

        continue


    if game_state == "victory":

        ui.draw_victory(
            screen,
            player.score
        )

        pygame.display.update()

        continue

    # ==========================================
    # PLAYER
    # ==========================================

    player.update()

    player.draw(screen)


    # ==========================================
    # PLAYER BULLET
    # ==========================================

    bullet.update()

    bullet.draw(screen)

    if shoot_timer > 0:
        shoot_timer -= 1

    if fire_button_held and not bullet.active and shoot_timer <= 0:

        laser_sound.play()

        bullet.fire(
            player.x + 18,
            player.y
        )

        shoot_timer = 5 if player.rapid_fire else shoot_delay


    # ==========================================
    # LEVEL
    # ==========================================

    level = player.score // LEVEL_KILLS + 1


    # ==========================================
    # BOSS SPAWN
    # ==========================================

    if level >= BOSS_LEVEL and not boss_spawned:

        boss.spawn()

        boss_spawned = True

        warning.start()


    # ==========================================
    # ENEMIES
    # ==========================================

    for enemy in enemies:

        if boss.active:
            break

        enemy.speed = ENEMY_SPEED + level * 0.25

        enemy.update()

        enemy.draw(screen)


        # -------------------------
        # Enemy reached player
        # -------------------------

        if enemy.y > HEIGHT - 170:

            player.hit()

            damage_flash.start()

            enemy.respawn()

            if player.lives <= 0:

                high_score = save_highscore(player.score)

                game_state = "game_over"


        # -------------------------
        # Bullet hits enemy
        # -------------------------

        if bullet.active:

            if bullet.get_rect().colliderect(
                    enemy.get_rect()):

                explosion_sound.play()

                explosion.start(
                    enemy.x,
                    enemy.y
                )

                bullet.reset()

                enemy.respawn()

                player.add_score(1)


                # Random Powerup
                if random.random() < POWERUP_DROP_CHANCE:

                    powerup.spawn(
                        enemy.x,
                        enemy.y
                    )


        # -------------------------
        # Enemy Shooting
        # -------------------------

        shot_roll = max(60, 250 - level * 8)

        if random.randint(1, shot_roll) == 1:

            for eb in enemy_bullets:

                if not eb.active:

                    eb.fire(
                        enemy.x + 25,
                        enemy.y + 40
                    )

                    break


    # ==========================================
    # ENEMY BULLETS
    # ==========================================

    for eb in enemy_bullets:

        eb.update()

        eb.draw(screen)

        if eb.active:

            if eb.get_rect().colliderect(

                    player.get_rect()):

                eb.reset()

                player.hit()

                damage_flash.start()

                if player.lives <= 0:

                    high_score = save_highscore(
                        player.score
                    )

                    game_state = "game_over"


    # ==========================================
    # POWERUPS
    # ==========================================

    powerup.move()

    powerup.draw(screen)

    if powerup.active:

        if powerup.get_rect().colliderect(

                player.get_rect()):

            powerup.apply(player,enemies)


    # ==========================================
    # BOSS
    # ==========================================

    if boss.active:

        boss.update()

        boss.draw(screen)

        boss.draw_health(screen)


        # Player bullet hits boss

        if bullet.active:

            if bullet.get_rect().colliderect(

                    boss.get_rect()):

                bullet.reset()

                explosion.start(

                    bullet.x,
                    bullet.y

                )

                dead = boss.damage()

                if dead:

                    player.add_score(50)

                    high_score = save_highscore(
                        player.score
                    )

                    game_state = "victory"


        # Boss shooting

        if boss.bullet_timer > 35:

            boss.bullet_timer = 0

            for bb in boss_bullets:

                if not bb.active:

                    bb.fire(

                        boss.x + BOSS_WIDTH//2,

                        boss.y + BOSS_HEIGHT

                    )

                    break


    # ==========================================
    # BOSS BULLETS
    # ==========================================

    for bb in boss_bullets:

        bb.update()

        bb.draw(screen)

        if bb.active:

            if bb.get_rect().colliderect(

                    player.get_rect()):

                bb.reset()

                player.hit()

                damage_flash.start()

                if player.lives <= 0:

                    high_score = save_highscore(
                        player.score
                    )

                    game_state = "game_over"

    # ==========================================
    # EFFECTS
    # ==========================================

    explosion.update()
    explosion.draw(screen)

    damage_flash.update()
    damage_flash.draw(screen)

    warning.update()
    warning.draw(screen)

    screen_shake.update()


    # ==========================================
    # RAPID FIRE TIMER
    # ==========================================

    if not player.rapid_fire:
        rapid_fire_timer = 0


    # ==========================================
    # UI
    # ==========================================

    ui.draw_score(
        screen,
        player.score,
        high_score
    )

    ui.draw_level(
        screen,
        level
    )

    ui.draw_lives(
        screen,
        player.lives
    )


    # ==========================================
    # FPS
    # ==========================================

    fps = int(clock.get_fps())

    ui.draw_fps(
        screen,
        fps
    )


    # ==========================================
    # DISPLAY
    # ==========================================

    pygame.display.update()

pygame.quit()