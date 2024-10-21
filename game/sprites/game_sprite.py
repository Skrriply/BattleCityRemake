from abc import ABC, abstractmethod
from typing import Optional

import pygame

from settings import window


class Movable(ABC):
    @abstractmethod
    def move(self) -> None:
        pass


class GameSprite(pygame.sprite.Sprite):
    """
    Клас ігрового спрайта.
    """

    def __init__(
        self,
        texture: str,
        x: float,
        y: float,
        width: int,
        height: int,
        speed: Optional[int] = None,
        hp: Optional[int] = None,
    ) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.hp = hp
        self.direction = None
        self.texture = pygame.transform.scale(
            pygame.image.load(texture), (width, height)
        )
        self.start_texture = self.texture.copy()
        self.rect = self.texture.get_rect(center=(x, y))

    def update_texture(self, texture: str) -> None:
        self.start_texture = pygame.transform.scale(pygame.image.load(texture), (self.width, self.height))
        self.texture = self.start_texture.copy()

    def rotate(self) -> None:
        angles = {"UP": 0, "DOWN": 180, "LEFT": 90, "RIGHT": -90}

        if self.direction in angles:
            angle = angles[self.direction]
            self.texture = pygame.transform.rotate(self.start_texture, angle)
            self.rect = self.texture.get_rect(
                center=(self.rect.centerx, self.rect.centery)
            )

    def draw(self) -> None:
        window.blit(self.texture, self.rect)
