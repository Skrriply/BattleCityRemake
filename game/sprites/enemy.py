import pygame

from settings import DEATH_SOUND, SOUNDS_VOLUME
from sprites.game_sprite import GameSprite, Movable


class Enemy(GameSprite, Movable):
    """
    Клас ворога.
    """

    def __init__(
        self,
        texture: str,
        x: float,
        y: float,
        width: int,
        height: int,
        speed: int,
        hp: int,
    ) -> None:
        super().__init__(texture, x, y, width, height, speed=speed, hp=hp)
        self.player_x = None
        self.player_y = None

    def move(self) -> None:
        if self.player_x and self.player_y:
            if self.rect.x < self.player_x:
                self.direction = "RIGHT"
                self.rect.x += self.speed
            elif self.rect.x > self.player_x:
                self.direction = "LEFT"
                self.rect.x -= self.speed

            if abs(self.rect.x - self.player_x) <= self.speed:
                if self.rect.y < self.player_y:
                    self.direction = "DOWN"
                    self.rect.y += self.speed
                elif self.rect.y > self.player_y:
                    self.direction = "UP"
                    self.rect.y -= self.speed

            self.rotate()

    def _check_collisions(self) -> None:
        # TODO: Додати зіткнення із гравцем та стінами
        pass

    def update(self, player_x: float, player_y: float) -> None:
        self.player_x, self.player_y = player_x, player_y
        self.move()
        self.draw()

        if self.hp <= 0:
            sound = pygame.mixer.Sound(DEATH_SOUND)
            sound.set_volume(SOUNDS_VOLUME)
            sound.play()
            self.kill()
