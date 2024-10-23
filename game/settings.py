from typing import Dict, Any, List

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
        self.volume = self.settings["volume"]


class ScreenManager:
    def __init__(self) -> None:
        self.screen = "MENU"

    def change_screen(self, screen: str) -> None:
        self.screen = screen


class SoundManager:
    def __init__(self, sound_paths: Dict[str, List[str]], volume: float) -> None:
        self.sound_paths = sound_paths
        self.volume = volume
        self.sounds = {}
        pygame.mixer.init()

    def load_sounds(self) -> None:
        for sound_name in self.sound_paths:
            path = normalize_path(*self.sound_paths[sound_name])
            self.sounds[sound_name] = pygame.mixer.Sound(path)
            self.sounds[sound_name].set_volume(self.volume)

    def play_sound(self, sound_name: str) -> None:
        if sound_name in self.sounds:
            self.sounds[sound_name].play()


# Завантажує налаштування з JSON
settings_manager = Settings()
GAME_SETTINGS = settings_manager.settings
COLORS = settings_manager.colors
TEXTURES = settings_manager.textures
SOUNDS = settings_manager.sounds
VOLUME = settings_manager.volume

# Константи
WINDOW_WIDTH = GAME_SETTINGS["window_width"]
WINDOW_HEIGHT = GAME_SETTINGS["window_height"]
FPS = GAME_SETTINGS["fps"]
PLAYER_FIRE_DELAY = GAME_SETTINGS["player_fire_delay"]
ENEMY_FIRE_DELAY = GAME_SETTINGS["enemy_fire_delay"]
MUSIC_VOLUME = VOLUME["music"]
SOUNDS_VOLUME = VOLUME["sounds"]

# Шлях до музики
BACKGROUND_MUSIC = normalize_path(*SOUNDS["background_music"])

# Змінні
screen_manager = ScreenManager()
sound_manager = SoundManager(SOUNDS, SOUNDS_VOLUME)
sound_manager.load_sounds()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Шляхи до текстур та файлів
PATH_TO_MAP = normalize_path(*GAME_SETTINGS["map"])
PLAYER_TEXTURE = normalize_path(*TEXTURES["player"])
ENEMY_TEXTURE = normalize_path(*TEXTURES["enemy"])
WALL_TEXTURE = normalize_path(*TEXTURES["wall"])
BULLET_TEXTURE = normalize_path(*TEXTURES["bullet"])
BACKGROUND_TEXTURE = normalize_path(*TEXTURES["background_menu"])
END_TEXTURE = normalize_path(*TEXTURES["end_menu"])
MEDKIT_TEXTURE = normalize_path(*TEXTURES["medkit"])

# Групи спрайтів
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
walls = pygame.sprite.Group()
