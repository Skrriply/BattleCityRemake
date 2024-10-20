import sys

import pygame

import game.sprites as sprites
from game.map import MapManager
from game.settings import (
    PLAYER_TEXTURE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    window,
    bullets,
    clock,
    FPS,
    BACKGROUND_TEXTURE,
    BACKGROUND_MUSIC,
    enemies,
    screen_manager,
    COLORS,
    walls,
)

# Змінення заголовка й іконки вікна
pygame.display.set_caption("Battle City Remake")
pygame.display.set_icon(pygame.image.load(PLAYER_TEXTURE))

# Музика
background_music = pygame.mixer.Sound(BACKGROUND_MUSIC)
background_music.set_volume(0.05)
background_music.play(-1)


class ButtonCallbacks:
    @staticmethod
    def start_game() -> None:
        screen_manager.change_screen("GAME")

    @staticmethod
    def exit() -> None:
        sys.exit()


class Game:
    def __init__(self) -> None:
        self.map_manager = MapManager()
        self._create_sprites()

    def _create_sprites(self) -> None:
        # Створення кнопок
        callbacks = ButtonCallbacks()
        self.start_button = sprites.Button(
            WINDOW_WIDTH / 2, 450, 150, 50, "Start", (12, 245, 12), callbacks.start_game
        )
        self.exit_button = sprites.Button(
            WINDOW_WIDTH / 2, 510, 150, 50, "Exit", (245, 12, 12), callbacks.exit
        )

        player_x, player_y = self.map_manager.load_map()
        
        # Створення гравця
        self.player = sprites.Player(PLAYER_TEXTURE, player_x, player_y, 100, 100, 5, 100)

    @staticmethod
    def _handle_events() -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def game_update(self) -> None:
        window.fill(COLORS["black"])
        walls.update()
        bullets.update()
        enemies.update()
        self.player.update()

    def menu_update(self) -> None:
        window.blit(
            pygame.transform.scale(
                pygame.image.load(BACKGROUND_TEXTURE), (WINDOW_WIDTH, WINDOW_HEIGHT)
            ),
            (0, 0),
        )
        self.start_button.update()
        self.exit_button.update()

    def run(self) -> None:
        while True:
            self._handle_events()

            if screen_manager.screen == "MENU":
                self.menu_update()
            elif screen_manager.screen == "GAME":
                self.game_update()

            pygame.display.update()
            clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
