import os

import pygame

pygame.init()

# Константи
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Кольори
BLACK = (0, 0, 0)

#Menu
BACKGROUND_MENU = os.path.join("textures", "background-menu.png")

# Спрайти
PLAYER_TEXTURE = os.path.join("textures", "player.png")
ENEMY_TEXTURE = os.path.join("textures", "player.png")
WALL_TEXTURE = os.path.join("textures", "player.png")

# Групи спрайтів
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
walls = pygame.sprite.Group()

# Вікно та годинник
screen = "menu"
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
