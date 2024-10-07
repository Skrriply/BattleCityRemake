import math
from typing import Callable

from settings import *


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, texture: str, x: int, y: int, width: int, height: int, speed: int) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.texture = pygame.transform.scale(pygame.image.load(texture), (width, height))
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


class Player(GameSprite):
    def __init__(self, image: str, x: int, y: int, width: int, height: int, speed: int) -> None:
        super().__init__(image, x, y, width, height, speed)
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


class Enemy(GameSprite):
    def __init__(self, image: str, x: int, y: int, width: int, height: int, speed: int) -> None:
        super().__init__(image, x, y, width, height, speed)
        self.hp = 100

    def spawn(self) -> None:
        pass

    def update(self) -> None:
        self.update_hitbox()
        # TODO: Додати ШІ бота


class Bullet(GameSprite):
    def __init__(self, image: str, x: int, y: int, width: int, height: int, speed: int, angle: float) -> None:
        super().__init__(image, x, y, width, height, speed)
        self.angle = angle

    def update(self) -> None:
        self.update_hitbox()
        self.rotate(math.degrees(-self.angle))
        self.rect.x += math.cos(self.angle) * self.speed
        self.rect.y += math.sin(self.angle) * self.speed

        if self.rect.x < 0 or self.rect.x > WINDOW_WIDTH or self.rect.y < 0 or self.rect.y > WINDOW_HEIGHT:
            self.kill()


class Wall(GameSprite):
    def __init__(self, image: str, x: int, y: int, width: int, height: int, speed: int) -> None:
        super().__init__(image, x, y, width, height, speed)
        self.hp = 100


class Button(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, text: str, color: tuple[int, int, int],
                 callback: Callable) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.callback = callback

        self._create_button(text)

    def _create_button(self, text: str) -> None:
        font = pygame.font.Font(None, 50)

        self.surface = pygame.Surface((self.width, self.height))
        self.rect = self.surface.get_rect(center=(self.x, self.y))

        self.label = font.render(text, True, WHITE)
        self.label_rect = self.label.get_rect(center=(self.width / 2, self.height / 2))

        self.surface.fill(self.color)
        self.surface.blit(self.label, self.label_rect)

    def change_color(self, color: tuple[int, int, int]) -> None:
        self.color = color

    def is_pressed(self) -> bool:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            if click[0] == 1:
                return True
        return False

    def update(self) -> None:
        if self.is_pressed():
            self.callback()
        self.surface.blit(self.label, self.label_rect)

    def draw(self) -> None:
        window.blit(self.surface, (self.rect.x, self.rect.y))