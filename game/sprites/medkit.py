from sprites.game_sprite import GameSprite


class Medkit(GameSprite):
    """
    Клас аптечки.
    """

    def __init__(
        self, texture: str, x: float, y: float, width: int, height: int, heal: int
    ) -> None:
        super().__init__(texture, x, y, width, height)
        self.heal = heal

    def update(self) -> None:
        self.draw()
