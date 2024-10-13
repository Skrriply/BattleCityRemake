from game.sprites.game_sprite import GameSprite, Movable

import time


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
        self.rotation_angle = 0
        self.endpos = False

    def spawn(self) -> None:
        pass

    def move(self) -> None:
        # TODO: Зробити нормальний ШІ для ворога
        if self.rect.centery >= 220 and self.endpos != True:
            self.rect.centery -= self.speed
            if self.rect.centery == 220:
                self.endpos = True
        if self.rect.centery >= 220 and self.endpos != False:
            self.rect.centery += self.speed



    def update(self) -> None:
        self.update_hitbox()

        if self.hp <= 0:
            self.kill()

        self.move()
