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
    def __init__(self, x, y, w, h, color, label, callback):
        super().__init__()
        if callback is not None:
            self.callback = callback
        else:
            print(callback)

        self.color = color
        r = color[0] + 15 if (color[0] + 15) <= 255 else 255
        g = color[1] + 15 if (color[1] + 15) <= 255 else 255
        b = color[2] + 15 if (color[2] + 15) <= 255 else 255

        self.light_color = (r, g, b)
        self.h = h
        self.w = w
        self.pressed = False

        self.surface = pygame.Surface((w, h))

        self.rect = self.surface.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.text = label
        self.label_rect = self.text.get_rect()
        self.label_rect.centerx = w / 2
        self.label_rect.centery = h / 2

        self.surface.fill(self.color)
        self.surface.blit(label, self.label_rect)

    def change_color(self, color):
        self.color = color
        r = color[0] + 15 if (color[0] + 15) <= 255 else 255
        g = color[1] + 15 if (color[1] + 15) <= 255 else 255
        b = color[2] + 15 if (color[2] + 15) <= 255 else 255
        self.light_color = (r, g, b)

    def is_on(self):
        x, y = pygame.mouse.get_pos()
        on = self.rect.collidepoint(x, y)
        if on:
            self.surface.fill(self.light_color)
        else:
            self.surface.fill(self.color)

        return on

    def is_press(self):
        bt = pygame.mouse.get_pressed()

        if self.is_on() and bt[0] and not self.pressed:
            self.pressed = True
            self.callback()
        if not bt[0]:
            self.pressed = False

    def update(self):
        self.is_press()
        self.surface.blit(self.text, self.label_rect)

    def draw(self):
        window.blit(self.surface, (self.rect.x, self.rect.y))
