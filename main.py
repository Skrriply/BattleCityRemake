import math
import pygame
#from settings import *

pygame.init()

"""Window"""
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Created window
clock = pygame.time.Clock() # Time FPS

pygame.display.set_caption("BattleCityRemake") # Name Window
#icon_game = pygame.image.load("") # Icon Window
#pygame.display.set_icon(icon_game) # Icon Window

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image: str, x: int, y: int, width: int, height: int, speed: int) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.texture = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.start_texture = self.texture

        self.rect = self.texture.get_rect()
        self.rect.center = (x, y)

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, width / 2, height / 2)

    def rotate(self, angle: float) -> None:
        self.texture = pygame.transform.rotate(self.start_texture, angle)
        self.rect = self.texture.get_rect(center=(self.rect.centerx, self.rect.centery))

    def draw(self) -> None:
        window.blit(self.texture, self.rect)


class Player(GameSprite):
    def __init__(self, image: str, x: int, y: int, width: int, height: int, speed: int) -> None:
        super().__init__(image, x, y, width, height, speed)
        self.max_hp = 100  # TODO: Змінити кільк. здоров'я
        self.hp = self.max_hp
        self.start_coords = (0, 0)  # TODO: Змінити координати
        self.score = 0

    def fire(self) -> None:
        # TODO: Додати звук вистрілу
        pass

    def update(self) -> None:
        self.hitbox.center = self.rect.center

        keys = pygame.key.get_pressed()
        buttons = pygame.mouse.get_pressed()

        # Керування WASD
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.centerx -= self.speed
        if keys[pygame.K_d] and self.rect.x < WINDOW_WIDTH - self.rect.width:
            self.rect.centerx += self.speed
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.centery -= self.speed
        if keys[pygame.K_s] and self.rect.y < WINDOW_HEIGHT - self.rect.height:
            self.rect.centery += self.speed

        if buttons[0]:
            self.fire()

        pos = pygame.mouse.get_pos()
        dx = pos[0] - self.rect.centerx
        dy = -(pos[1] - self.rect.centery)
        ang = math.degrees(math.atan2(dy, dx))

        self.rotate(ang - 90)


class Enemy:
    def __init__(self, image: str, x: int, y: int, width: int, height: int, speed: int) -> None:
        super().__init__(image, x, y, width, height, speed)
        self.max_hp = 100  # TODO: Змінити кільк. здоров'я
        self.hp = self.max_hp
        self.start_coords = (0, 0)  # TODO: Змінити координати

    def spawn(self) -> None:
        pass

    def update(self) -> None:
        pass


class Bullet(GameSprite):
    def __init__(self, image: str, x: int, y: int, width: int, height: int, speed: int, angle: float) -> None:
        super().__init__(image, x, y, width, height, speed)
        self.angle = angle

    def update(self) -> None:
        self.hitbox.center = self.rect.center
        self.rotate(math.degrees(-self.angle) - 90)
        self.rect.x += math.cos(self.angle) * self.speed
        self.rect.y += math.sin(self.angle) * self.speed


class Wall(GameSprite):
    def __init__(self, image: str, x: int, y: int, width: int, height: int, speed: int) -> None:
        super().__init__(image, x, y, width, height, speed)
        self.max_hp = 100  # TODO: Змінити кільк. здоров'я
        self.hp = self.max_hp
        self.start_coords = (0, 0)  # TODO: Змінити координати

    def update(self) -> None:
        pass


class Button(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple[int], label: str) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.label = label

    def change_color(self) -> None:
        pass

    def is_pressed(self) -> bool:
        pass

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass


screen = "menu"
game = True

while game:
    if screen == "menu":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False  


    if screen == "game":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False 
    
    
    if screen == "pause":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False 