import pygame

from game.settings import WINDOW_WIDTH, WINDOW_HEIGHT
from game.sprites.game_sprite import GameSprite


class Player(GameSprite):
    """
    Клас гравця.
    """

    def __init__(
        self, texture: str, x: float, y: float, width: int, height: int, speed: int
    ) -> None:
        super().__init__(texture, x, y, width, height, speed)
        self.hp = 100
        self.score = 0
        self.angle = 0

    def fire(self) -> None:
        # TODO: Зробити механіку вистрілу
        pass

    def process_input(self) -> None:
        keys = pygame.key.get_pressed()
        buttons = pygame.mouse.get_pressed()

        # Керування з клавіатури
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.centerx -= self.speed
            self.angle = 90
        elif keys[pygame.K_d] and self.rect.x < WINDOW_WIDTH - self.rect.width:
            self.rect.centerx += self.speed
            self.angle = -90
        elif keys[pygame.K_w] and self.rect.y > 0:
            self.rect.centery -= self.speed
            self.angle = 0
        elif keys[pygame.K_s] and self.rect.y < WINDOW_HEIGHT - self.rect.height:
            self.rect.centery += self.speed
            self.angle = 180

        self.rotate(self.angle)

        # Керування з мишки
        if buttons[0]:
            self.fire()

    def update(self) -> None:
        self.update_hitbox()
        self.process_input()
