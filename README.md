# Battle for the Quest of Tsundere

Battle for the Quest of Tsundere is a fast-paced 2D arcade shooter built with Python and Pygame.
Pilot your hero ship, survive escalating enemy waves, collect power-ups, and defeat the boss to win.

## Features

- Arcade-style movement and shooting with responsive controls.
- Progressive difficulty with enemy speed scaling by level.
- Multiple enemy types (normal, fast, tank) with different behaviors.
- Power-up system:
  - Extra life
  - Shield
  - Rapid fire
  - Bomb clear
- Boss encounter with a dedicated health bar and projectile attacks.
- Visual effects (explosion, warning banner, damage flash).
- Persistent high score saved to disk.

## Tech Stack

- Python 3.x
- Pygame

## Quick Start

1. Clone the repository:

	```bash
	git clone https://github.com/Exit0Hero/Battle-for-the-Quest-o-Tsundere.git
	cd Battle-for-the-Quest-o-Tsundere
	```

2. Install dependencies:

	```bash
	pip install pygame
	```

3. Run the game:

	```bash
	python game.py
	```

## Controls

- Left Arrow: Move left
- Right Arrow: Move right
- Space: Shoot (hold for continuous fire)
- P: Pause / Resume
- R: Restart (from game over or victory screen)
- Esc: Quit (from menu or end screens)

## Game Flow

1. Start from the menu screen.
2. Defeat enemies to increase score and level.
3. Survive enemy bullets and collisions using lives and power-ups.
4. Reach the boss level and defeat the boss to win.

## Project Structure

- `game.py`: Main game loop and state handling.
- `settings.py`: Shared configuration constants.
- `player.py`: Player movement, lives, and power-up states.
- `enemy.py`: Enemy spawning and movement.
- `bullet.py`: Player and enemy bullet classes.
- `boss.py`: Boss logic, health, and boss bullets.
- `powerups.py`: Power-up spawning and effects.
- `effects.py`: Explosion, warning, flash, and shake effects.
- `ui.py`: Menu and HUD rendering.
- `save.py`: High score load/save helpers.

## Assets

All game assets are stored under the `assets/` directory.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
