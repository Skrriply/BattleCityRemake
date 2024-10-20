from abc import ABC, abstractmethod
from typing import Union

import pygame

from game.settings import window


class Movable(ABC):
    @abstractmethod
    def move(self) -> None:
        pass


class GameSprite(pygame.sprite.Sprite):
    """
    Клас ігрового спрайта.
    """

    def __init__(
        self, texture: str, x: float, y: float, width: int, height: int, speed: Union[int] = None, hp: Union[int] = None
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

    def rotate(self) -> None:
        if self.direction == "UP":
            angle = 0
        elif self.direction == "DOWN":
            angle = 180
        elif self.direction == "LEFT":
            angle = 90
        elif self.direction == "RIGHT":
            angle = -90
        
        if self.direction:
            self.texture = pygame.transform.rotate(self.start_texture, angle)
            self.rect = self.texture.get_rect(center=(self.rect.centerx, self.rect.centery))

    def draw(self) -> None:
        window.blit(self.texture, self.rect)
