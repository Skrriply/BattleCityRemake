import sys

import pygame

import sprites as sprites
from map import MapManager
from settings import (
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
    END_TEXTURE,
)

# Змінення заголовка й іконки вікна
pygame.display.set_caption("Battle City Remake")
pygame.display.set_icon(pygame.image.load(PLAYER_TEXTURE))

# Музика
background_music = pygame.mixer.Sound(BACKGROUND_MUSIC)
background_music.set_volume(0.05)
background_music.play(-1)


class Game:
    def __init__(self) -> None:
        self.map_manager = MapManager()
        self._create_sprites()

    def _create_sprites(self) -> None:
        # Створення кнопок
        callbacks = sprites.ButtonCallbacks()
        self.start_button = sprites.Button(
            WINDOW_WIDTH / 2, 450, 150, 50, "Start", (12, 245, 12), callbacks.start_game
        )
        self.continue_button = sprites.Button(
            WINDOW_WIDTH / 2, 450, 150, 50, "Start", (12, 245, 12), callbacks.start_game
        )
        self.exit_button = sprites.Button(
            WINDOW_WIDTH / 2, 510, 150, 50, "Exit", (245, 12, 12), callbacks.exit
        )
        self.retry_button = sprites.Button(
            WINDOW_WIDTH / 2, 510, 150, 50, "Retry", (245, 12, 12), callbacks.start_game
        )

        # Створення гравця та мапи
        player_x, player_y = self.map_manager.load_map()
        self.player = sprites.Player(
            PLAYER_TEXTURE, player_x, player_y, 85, 100, 5, 100
        )

    @staticmethod
    def _handle_events() -> None:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif keys[pygame.K_ESCAPE]:
                screen = screen_manager.screen
                if screen == "GAME":
                    screen_manager.change_screen("PAUSE")
                elif screen == "PAUSE" and screen not in ["MENU", "END"]:
                    screen_manager.change_screen("GAME")

    def _game_update(self) -> None:
        window.fill(COLORS["black"])
        walls.update()
        bullets.update()
        enemies.update(self.player.rect.x, self.player.rect.y)
        self.player.update()

    def _menu_update(self) -> None:
        window.blit(
            pygame.transform.scale(
                pygame.image.load(BACKGROUND_TEXTURE), (WINDOW_WIDTH, WINDOW_HEIGHT)
            ),
            (0, 0),
        )
        self.start_button.update()
        self.exit_button.update()

    def _end_update(self) -> None:
        window.blit(
            pygame.transform.scale(
                pygame.image.load(END_TEXTURE), (WINDOW_WIDTH, WINDOW_HEIGHT)
            ),
            (0, 0),
        )
        self.player.hp = 100
        self.start_button.update()
        self.exit_button.update()

    def _pause_update(self) -> None:
        self.continue_button.update()
        self.exit_button.update()

    def _update_screen(self) -> None:
        window.fill(COLORS["black"])
        if screen_manager.screen == "MENU":
            self._menu_update()
        elif screen_manager.screen == "GAME":
            self._game_update()
        elif screen_manager.screen == "END":
            self._end_update()
        elif screen_manager.screen == "PAUSE":
            self._pause_update()

        pygame.display.update()
        clock.tick(FPS)

    def run(self) -> None:
        while True:
            self._handle_events()
            self._update_screen()


if __name__ == "__main__":
    game = Game()
    game.run()
