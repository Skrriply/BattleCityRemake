from game.sprites.game_sprite import GameSprite, Movable


class Enemy(GameSprite, Movable):
    """
    Клас ворога.
    """

    def __init__(
        self, texture: str, x: float, y: float, width: int, height: int, speed: int
    ) -> None:
        super().__init__(texture, x, y, width, height)
        self.speed = speed
        self.hp = 100

    def spawn(self) -> None:
        pass

    def move(self) -> None:
        # TODO: Додати ШІ бота
        pass

    def update(self) -> None:
        self.update_hitbox()
        self.move()
