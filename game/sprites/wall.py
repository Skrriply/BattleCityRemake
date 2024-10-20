import pygame

from game.settings import WALL_DESTROYED_SOUND
from game.sprites.game_sprite import GameSprite


class Wall(GameSprite):
    """
    Клас стіни.
    """

    def __init__(
        self, texture: str, x: float, y: float, width: int, height: int, hp: int
    ) -> None:
        super().__init__(texture, x, y, width, height, hp=hp)

    def update(self) -> None:
        self.draw()

        # Знищення стіни
        if self.hp <= 0:
            pygame.mixer.Sound(WALL_DESTROYED_SOUND).play()
            self.kill()
