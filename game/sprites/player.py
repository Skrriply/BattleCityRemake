import pygame

from settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    walls,
    bullets,
    BULLET_TEXTURE,
    PLAYER_FIRE_DELAY,
    screen_manager,
    sound_manager,
)
from sprites.bullet import Bullet
from sprites.game_sprite import GameSprite, Movable


class Player(GameSprite, Movable):
    """
    Клас гравця.
    """

    def __init__(
        self,
        texture: str,
        x: float,
        y: float,
        width: int,
        height: int,
        speed: int,
        hp: int,
    ) -> None:
        super().__init__(texture, x, y, width, height, speed=speed, hp=hp)
        self.last_fire_time = pygame.time.get_ticks()  # Час останнього пострілу

    def fire(self) -> None:
        current_time = pygame.time.get_ticks()

        if current_time - self.last_fire_time >= PLAYER_FIRE_DELAY:
            sound_manager.play_sound("fire")
            bullet = Bullet(
                BULLET_TEXTURE,
                self.rect.centerx,
                self.rect.centery,
                50,
                50,
                10,
                self.direction,
                40,
                "PLAYER",
            )
            bullets.add(bullet)
            self.last_fire_time = current_time  # Оновлюємо час останнього пострілу

    def move(self) -> None:
        previous_coords = self.rect.copy()

        if self.direction == "UP":
            self.rect.centery -= self.speed
        elif self.direction == "DOWN":
            self.rect.centery += self.speed
        elif self.direction == "LEFT":
            self.rect.centerx -= self.speed
        elif self.direction == "RIGHT":
            self.rect.centerx += self.speed

        if pygame.sprite.spritecollide(self, walls, False):
            self.rect = previous_coords

        self.rotate()

    def process_input(self) -> None:
        keys = pygame.key.get_pressed()

        # Керування з клавіатури
        if keys[pygame.K_w] and self.rect.y > 0:
            self.direction = "UP"
            self.move()
        elif keys[pygame.K_s] and self.rect.y < WINDOW_HEIGHT - self.rect.height:
            self.direction = "DOWN"
            self.move()
        elif keys[pygame.K_a] and self.rect.x > 0:
            self.direction = "LEFT"
            self.move()
        elif keys[pygame.K_d] and self.rect.x < WINDOW_WIDTH - self.rect.width:
            self.direction = "RIGHT"
            self.move()

        if keys[pygame.K_SPACE] and self.direction:
            self.fire()

    def update(self) -> None:
        self.process_input()
        self.draw()

        if self.hp <= 0:
            sound_manager.play_sound("death")
            self.kill()
            screen_manager.change_screen("END")
