import sys

import pygame

import game.sprites as sprites
from game.settings import (
    PLAYER_TEXTURE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    window,
    bullets,
    clock,
    FPS,
    BACKGROUND_TEXTURE,
    screen,
    COLORS,
    walls,
    WALL_TEXTURE
)

# Змінення заголовка й іконки вікна
pygame.display.set_caption("Battle City Remake")
pygame.display.set_icon(pygame.image.load(PLAYER_TEXTURE))


class ButtonCallbacks:
    @staticmethod
    def start_game() -> None:
        global screen
        screen = "game"

    @staticmethod
    def exit() -> None:
        sys.exit()


class Game:
    def __init__(self) -> None:
        self._create_sprites()

    def _create_sprites(self) -> None:
        callbacks = ButtonCallbacks()
        self.start_button = sprites.Button(
            WINDOW_WIDTH / 2, 450, 150, 50, "Start", (12, 245, 12), callbacks.start_game
        )
        self.exit_button = sprites.Button(
            WINDOW_WIDTH / 2, 510, 150, 50, "Exit", (245, 12, 12), callbacks.exit
        )
        self.player = sprites.Player(
            PLAYER_TEXTURE, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 100, 100, 5
        )
        created_walls = [
            sprites.Wall(WALL_TEXTURE, 100, 100, 100, 100),
            sprites.Wall(WALL_TEXTURE, 200, 150, 100, 100),
            sprites.Wall(WALL_TEXTURE, 300, 200, 100, 100),
            sprites.Wall(WALL_TEXTURE, 500, 300, 100, 100),   
        ]
        for wall in created_walls:
            walls.add(wall)

    @staticmethod
    def _handle_events() -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def game_update(self) -> None:
        # TODO: Додати оновлення ворогів та стін
        window.fill(COLORS["black"])

        self.player.update()
        self.player.draw()
        
        for wall in walls:
            wall.update()
            wall.draw()

        for bullet in bullets:
            bullet.update()
            bullet.draw()

    def menu_update(self) -> None:
        window.blit(
            pygame.transform.scale(
                pygame.image.load(BACKGROUND_TEXTURE), (WINDOW_WIDTH, WINDOW_HEIGHT)
            ),
            (0, 0),
        )
        self.start_button.update()
        self.start_button.draw()
        self.exit_button.update()
        self.exit_button.draw()

    def run(self) -> None:
        while True:
            self._handle_events()

            if screen == "menu":
                self.menu_update()
            elif screen == "game":
                self.game_update()

            pygame.display.update()
            clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
