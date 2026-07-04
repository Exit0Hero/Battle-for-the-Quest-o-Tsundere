# ===============================
# SCREEN
# ===============================

WIDTH = 800
HEIGHT = 600
FPS = 120

# ===============================
# PLAYER
# ===============================

PLAYER_SPEED = 0.8
PLAYER_START_X = 370
PLAYER_START_Y = 480

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100

PLAYER_LIVES = 3

# ===============================
# PLAYER BULLETS
# ===============================

PLAYER_BULLET_SPEED = 8
PLAYER_BULLET_WIDTH = 20
PLAYER_BULLET_HEIGHT = 40

# ===============================
# ENEMY
# ===============================

NUM_ENEMIES = 6

ENEMY_WIDTH = 64
ENEMY_HEIGHT = 64

NORMAL_SPEED = 0.8
FAST_SPEED = 1.5
TANK_SPEED = 0.5

ENEMY_DROP = 50
ENEMY_SPEED = 0.8

LEVEL_KILLS = 10

# ===============================
# ENEMY BULLETS
# ===============================

ENEMY_BULLET_SPEED = 3
ENEMY_BULLET_WIDTH = 12
ENEMY_BULLET_HEIGHT = 28

# ===============================
# BOSS
# ===============================

BOSS_WIDTH = 200
BOSS_HEIGHT = 200

BOSS_SPEED = 3

BOSS_HEALTH = 100

BOSS_LEVEL = 5

# ===============================
# POWERUPS
# ===============================

POWERUP_SIZE = 48
POWERUP_SPEED = 3

POWERUP_DROP_CHANCE = 0.20

# ===============================
# COLORS
# ===============================

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,255,255)
YELLOW = (255,255,0)
GRAY = (120,120,120)

# ===============================
# GAME
# ===============================

GAME_TITLE = "Battle for the quest of Tsundere"

GAME_STATES = [
    "menu",
    "playing",
    "paused",
    "game_over",
    "victory"
]