import sys

import objects
from settings import *

pygame.init()

# Змінення заголовка й іконки вікна
pygame.display.set_caption("Battle City Remake")
pygame.display.set_icon(pygame.image.load(PLAYER_TEXTURE))


class Game:
    def __init__(self) -> None:
        self._create_sprites()

    def _create_sprites(self) -> None:
        self.player = objects.Player(PLAYER_TEXTURE, 0, 0, 100, 100, 5)
        self.enemy = objects.Enemy(ENEMY_TEXTURE, 0, 0, 100, 100, 5)

    @staticmethod
    def _handle_events() -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update(self) -> None:
        # TODO: Додати оновлення ворогів та стін
        window.fill(BLACK)

        self.player.update()
        self.player.draw()

        for bullet in bullets:
            bullet.update()
            bullet.draw()

    def run(self) -> None:
        while True:
            if screen == "menu":
                self._handle_events()

                window.blit(pygame.transform.scale(pygame.image.load(BACKGROUND_MENU), (WINDOW_WIDTH, WINDOW_HEIGHT)), (0, 0))
                btn = objects.Button(400, 400, 300, 100, (255, 0, 0), "Start")
                btn.update()

                pygame.display.update()
                clock.tick(FPS)


            if screen == "game":
                self._handle_events()
                self.update()

                pygame.display.update()
                clock.tick(FPS)



if __name__ == "__main__":
    game = Game()
    game.run()
