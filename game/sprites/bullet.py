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
        self.rotation_angle = angle

    def move(self) -> None:
        # Текстура кулі типово повернута праворуч
        if self.rotation_angle == 0:  # Вгору
            self.rotate(90)
            self.rect.centery -= self.speed
        elif self.rotation_angle == 90:  # Ліворуч
            self.rotate(180)
            self.rect.centerx -= self.speed
        elif self.rotation_angle == 180:  # Вниз
            self.rotate(-90)
            self.rect.centery += self.speed
        elif self.rotation_angle == -90:  # Праворуч
            self.rotate(0)
            self.rect.centerx += self.speed

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
