import sys

import objects
from settings import *

pygame.init()

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
        self.start_button = objects.Button(
            WINDOW_WIDTH / 2, 450, 150, 50, "Start", (12, 245, 12), callbacks.start_game
        )
        self.exit_button = objects.Button(
            WINDOW_WIDTH / 2, 510, 150, 50, "Exit", (245, 12, 12), callbacks.exit
        )
        self.player = objects.Player(
            PLAYER_TEXTURE, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 100, 100, 5
        )
        # self.enemy = objects.Enemy(ENEMY_TEXTURE, 0, 0, 100, 100, 5)

    @staticmethod
    def _handle_events() -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def game_update(self) -> None:
        # TODO: Додати оновлення ворогів та стін
        window.fill(BLACK)

        self.player.update()
        self.player.draw()

        for bullet in bullets:
            bullet.update()
            bullet.draw()

    def menu_update(self) -> None:
        window.blit(
            pygame.transform.scale(BACKGROUND_MENU, (WINDOW_WIDTH, WINDOW_HEIGHT)),
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
