from game.sprites.game_sprite import GameSprite
import pygame


class Wall(GameSprite):
    """
    Клас стіни.
    """

    def __init__(
        self, texture: str, x: float, y: float, width: int, height: int
    ) -> None:
        super().__init__(texture, x, y, width, height)
        self.hp = 100

    def update(self) -> None:
        self.update_hitbox()

        # Знищення стіни
        if self.hp <= 0:
            self.kill()
            wall = pygame.mixer.Sound('sounds\\wall_destroyed.wav')
            wall.play()
