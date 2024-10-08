import pygame

from game.settings import WINDOW_WIDTH, WINDOW_HEIGHT, walls
from game.sprites.game_sprite import GameSprite, Movable


class Player(GameSprite, Movable):
    """
    Клас гравця.
    """

    def __init__(
        self, texture: str, x: float, y: float, width: int, height: int, speed: int
    ) -> None:
        super().__init__(texture, x, y, width, height)
        self.speed = speed
        self.hp = 100
        self.score = 0
        self.rotation_angle = 0

    def fire(self) -> None:
        # TODO: Зробити механіку вистрілу
        pass
    
    def move(self) -> None:
        previous_coords = self.rect.copy()

        if self.rotation_angle == 0:  # Вгору
            self.rect.centery -= self.speed
        elif self.rotation_angle == 90:  # Ліворуч
            self.rect.centerx -= self.speed
        elif self.rotation_angle == 180:  # Вниз
            self.rect.centery += self.speed
        elif self.rotation_angle == -90:  # Праворуч
            self.rect.centerx += self.speed

        if pygame.sprite.spritecollide(self, walls, False):
            self.rect = previous_coords
        else:
            self.rotate(self.rotation_angle)

    def process_input(self) -> None:
        keys = pygame.key.get_pressed()
        buttons = pygame.mouse.get_pressed()

        # Керування з клавіатури
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rotation_angle = 90
            self.move()
        elif keys[pygame.K_d] and self.rect.x < WINDOW_WIDTH - self.rect.width:
            self.rotation_angle = -90
            self.move()
        elif keys[pygame.K_w] and self.rect.y > 0:
            self.rotation_angle = 0
            self.move()
        elif keys[pygame.K_s] and self.rect.y < WINDOW_HEIGHT - self.rect.height:
            self.rotation_angle = 180
            self.move()

        # Керування з мишки
        if buttons[0]:
            self.fire()

    def update(self) -> None:
        self.update_hitbox()
        self.process_input()
