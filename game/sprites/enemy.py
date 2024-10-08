from game.sprites.game_sprite import GameSprite


class Enemy(GameSprite):
    """
    Клас ворога.
    """

    def __init__(
        self, texture: str, x: float, y: float, width: int, height: int, speed: int
    ) -> None:
        super().__init__(texture, x, y, width, height, speed)
        self.hp = 100

    def spawn(self) -> None:
        pass

    def update(self) -> None:
        self.update_hitbox()
        # TODO: Додати ШІ бота
