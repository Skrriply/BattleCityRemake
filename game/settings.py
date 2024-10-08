import json
from typing import Dict, Any

import pygame

import game.utils as utils


class Settings:
    def __init__(self) -> None:
        self._init_settings()

    @staticmethod
    def _load_settings() -> Dict[str, Any]:
        path_to_settings = utils.normalize_path("config", "settings.json")
        with open(path_to_settings, "r", encoding="utf-8") as file:
            return json.load(file)

    def _init_settings(self) -> None:
        # Змінні
        self.settings = self._load_settings()
        self.colors = self.settings["colors"]
        self.textures = self.settings["textures"]


# Завантажує налаштування з JSON
settings_manager = Settings()
GAME_SETTINGS = settings_manager.settings
COLORS = settings_manager.colors
TEXTURES = settings_manager.textures

# Константи
WINDOW_WIDTH = GAME_SETTINGS["window_width"]
WINDOW_HEIGHT = GAME_SETTINGS["window_height"]
FPS = GAME_SETTINGS["fps"]

# Змінні
screen = "menu"
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Шляхи до текстур
PLAYER_TEXTURE = utils.normalize_path(*TEXTURES["player"])
ENEMY_TEXTURE = utils.normalize_path(*TEXTURES["enemy"])
WALL_TEXTURE = utils.normalize_path(*TEXTURES["wall"])
BULLET_TEXTURE = utils.normalize_path(*TEXTURES["bullet"])
BACKGROUND_TEXTURE = utils.normalize_path(*TEXTURES["background_menu"])

# Групи спрайтів
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
walls = pygame.sprite.Group()
