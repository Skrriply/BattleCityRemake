from typing import Dict, Any

import pygame

from utils import open_file, normalize_path


class Settings:
    def __init__(self) -> None:
        self._init_settings()

    @staticmethod
    def _load_settings() -> Dict[str, Any]:
        path_to_settings = normalize_path("config", "settings.json")
        return open_file(path_to_settings, is_json=True)

    def _init_settings(self) -> None:
        # Змінні
        self.settings = self._load_settings()
        self.colors = self.settings["colors"]
        self.textures = self.settings["textures"]
        self.sounds = self.settings["sounds"]


class ScreenManager:
    def __init__(self) -> None:
        self.screen = "MENU"

    def change_screen(self, screen: str) -> None:
        self.screen = screen


# Завантажує налаштування з JSON
settings_manager = Settings()
GAME_SETTINGS = settings_manager.settings
COLORS = settings_manager.colors
TEXTURES = settings_manager.textures
SOUNDS = settings_manager.sounds

# Константи
WINDOW_WIDTH = GAME_SETTINGS["window_width"]
WINDOW_HEIGHT = GAME_SETTINGS["window_height"]
FPS = GAME_SETTINGS["fps"]
FIRE_DELAY = GAME_SETTINGS["fire_delay"]

# Змінні
screen_manager = ScreenManager()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Шляхи до текстур та файлів
PATH_TO_MAP = normalize_path(*GAME_SETTINGS["map"])
PLAYER_TEXTURE = normalize_path(*TEXTURES["player"])
ENEMY_TEXTURE = normalize_path(*TEXTURES["enemy"])
WALL_TEXTURE = normalize_path(*TEXTURES["wall"])
BULLET_TEXTURE = normalize_path(*TEXTURES["bullet"])
BACKGROUND_TEXTURE = normalize_path(*TEXTURES["background_menu"])

# Шляхи до звуків та музики
BACKGROUND_MUSIC = normalize_path(*SOUNDS["background_music"])
FIRE_SOUND = normalize_path(*SOUNDS["fire"])
WALL_DESTROYED_SOUND = normalize_path(*SOUNDS["wall_destroyed"])
DEATH_SOUND = normalize_path(*SOUNDS["death"])
HIT_SOUND = normalize_path(*SOUNDS["hit"])
WALL_HIT_SOUND = normalize_path(*SOUNDS["wall_hit"])

# Групи спрайтів
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
walls = pygame.sprite.Group()
