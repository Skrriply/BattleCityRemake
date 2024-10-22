from settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)
from sprites.game_sprite import GameSprite, Movable


class Bullet(GameSprite, Movable):
    """
    Клас кулі.
    """

    def __init__(
        self,
        texture: str,
        x: float,
        y: float,
        width: int,
        height: int,
        speed: int,
        direction: str,
        damage: int,
        owned_by: int,
    ) -> None:
        super().__init__(texture, x, y, width, height, speed=speed)
        self.direction = direction
        self.damage = damage
        self.owned_by = owned_by

    def move(self) -> None:
        if self.direction == "UP":
            self.rect.centery -= self.speed
        elif self.direction == "DOWN":
            self.rect.centery += self.speed
        elif self.direction == "LEFT":
            self.rect.centerx -= self.speed
        elif self.direction == "RIGHT":
            self.rect.centerx += self.speed

        # Видаляє кулю, якщо вона вийшла за ігрове вікно
        if (
            self.rect.x < 0
            or self.rect.x > WINDOW_WIDTH
            or self.rect.y < 0
            or self.rect.y > WINDOW_HEIGHT
        ):
            self.kill()

        self.rotate()

    def update(self) -> None:
        self.move()
        self.draw()
