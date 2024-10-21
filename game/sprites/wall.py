import pygame

from settings import WALL_DESTROYED_SOUND, SOUNDS_VOLUME
from sprites.game_sprite import GameSprite


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
            sound = pygame.mixer.Sound(WALL_DESTROYED_SOUND)
            sound.set_volume(SOUNDS_VOLUME)
            sound.play()
            self.kill()
