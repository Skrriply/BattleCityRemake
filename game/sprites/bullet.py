from game.settings import WINDOW_WIDTH, WINDOW_HEIGHT
from game.sprites.game_sprite import GameSprite


class Bullet(GameSprite):
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
        super().__init__(texture, x, y, width, height, speed)
        self.angle = angle

    def update(self) -> None:
        self.update_hitbox()
        # TODO: Додати рух кулі

        # Видаляє кулю, якщо вона вийшла за ігрове вікно
        if (
            self.rect.x < 0
            or self.rect.x > WINDOW_WIDTH
            or self.rect.y < 0
            or self.rect.y > WINDOW_HEIGHT
        ):
            self.kill()
