from game.settings import WINDOW_WIDTH, WINDOW_HEIGHT
from game.sprites.game_sprite import GameSprite, Movable


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
        angle: float,
    ) -> None:
        super().__init__(texture, x, y, width, height)
        self.speed = speed
        self.angle = angle

    def move(self) -> None:
        # TODO: Додати рух кулі

        # Видаляє кулю, якщо вона вийшла за ігрове вікно
        if (
            self.rect.x < 0
            or self.rect.x > WINDOW_WIDTH
            or self.rect.y < 0
            or self.rect.y > WINDOW_HEIGHT
        ):
            self.kill()

    def update(self) -> None:
        self.update_hitbox()
        self.move()
