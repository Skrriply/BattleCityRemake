import pygame

from game.settings import window


class GameSprite(pygame.sprite.Sprite):
    """
    Клас ігрового спрайта.
    """

    def __init__(
        self, texture: str, x: float, y: float, width: int, height: int, speed: int
    ) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.texture = pygame.transform.scale(
            pygame.image.load(texture), (width, height)
        )
        self.start_texture = self.texture
        self.rect = self.texture.get_rect(center=(x, y))
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, width / 2, height / 2)

    def rotate(self, angle: float) -> None:
        self.texture = pygame.transform.rotate(self.start_texture, angle)
        self.rect = self.texture.get_rect(center=(self.rect.centerx, self.rect.centery))

    def update_hitbox(self) -> None:
        self.hitbox.center = self.rect.center

    def draw(self) -> None:
        window.blit(self.texture, self.rect)
