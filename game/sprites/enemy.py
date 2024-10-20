from game.sprites.game_sprite import GameSprite, Movable


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
        # self.direction = None

    def spawn(self) -> None:
        pass

    def move(self) -> None:
        # TODO: Додати логіку руху через стратегії
        pass

    def update(self) -> None:
        self.move()
        self.draw()
