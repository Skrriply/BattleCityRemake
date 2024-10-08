from typing import Tuple, Callable

import pygame

from game.settings import COLORS, window

pygame.init()


class Button(pygame.sprite.Sprite):
    """
    Клас кнопки.
    """

    def __init__(
        self,
        x: float,
        y: float,
        width: int,
        height: int,
        text: str,
        color: Tuple[int, int, int],
        callback: Callable,
    ) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.light_color = self.calculate_light_color(self.color)
        self.callback = callback

        self._create_button(text)

    def _create_button(self, text: str) -> None:
        font = pygame.font.Font(None, 50)
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = self.surface.get_rect(center=(self.x, self.y))
        self.label = font.render(text, True, COLORS["white"])
        self.label_rect = self.label.get_rect(center=(self.width / 2, self.height / 2))
        self.surface.fill(self.color)
        self.surface.blit(self.label, self.label_rect)

    @staticmethod
    def calculate_light_color(color: Tuple[int, int, int]) -> Tuple[int, int, int]:
        return tuple(min(c + 15, 255) for c in color)

    def is_on(self) -> bool:
        x, y = pygame.mouse.get_pos()
        is_on = self.rect.collidepoint(x, y)

        # Ефект при наведенні на кнопку
        if is_on:
            self.surface.fill(self.light_color)
        else:
            self.surface.fill(self.color)

        return is_on

    def is_pressed(self) -> bool:
        buttons = pygame.mouse.get_pressed()

        if self.is_on() and buttons[0]:
            return True
        return False

    def update(self) -> None:
        if self.is_pressed():
            self.callback()

        self.surface.blit(self.label, self.label_rect)

    def draw(self) -> None:
        window.blit(self.surface, (self.rect.x, self.rect.y))
