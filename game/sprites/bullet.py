import pygame

from game.settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    walls,
    enemies,
    HIT_SOUND,
    WALL_HIT_SOUND,
)
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
        direction: str,
        damage: int,
    ) -> None:
        super().__init__(texture, x, y, width, height, speed=speed)
        self.direction = direction
        self.damage = damage

    def move(self) -> None:
        if self.direction == "UP":
            self.rect.centery -= self.speed
        elif self.direction == "DOWN":
            self.rect.centery += self.speed
        elif self.direction == "LEFT":
            self.rect.centerx -= self.speed
        elif self.direction == "RIGHT":
            self.rect.centerx += self.speed

        self.rotate()

    def _check_collisions(self) -> None:
        # Видаляє кулю, якщо вона вийшла за ігрове вікно
        if (
            self.rect.x < 0
            or self.rect.x > WINDOW_WIDTH
            or self.rect.y < 0
            or self.rect.y > WINDOW_HEIGHT
        ):
            self.kill()

        # Взаємодія із стіною
        collided_walls = pygame.sprite.spritecollide(self, walls, False)
        if collided_walls:
            sound = pygame.mixer.Sound(WALL_HIT_SOUND)
            sound.set_volume(0.25)
            sound.play()
            self.kill()
            wall = collided_walls[0]
            wall.hp -= self.damage

        # Взаємодія із ворогом
        collided_enemies = pygame.sprite.spritecollide(self, enemies, False)
        if collided_enemies:
            sound = pygame.mixer.Sound(HIT_SOUND)
            sound.set_volume(0.25)
            sound.play()
            self.kill()
            enemy = collided_enemies[0]
            enemy.hp -= self.damage

    def update(self) -> None:
        self.move()
        self._check_collisions()
        self.draw()
