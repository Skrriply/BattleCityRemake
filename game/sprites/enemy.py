import pygame
from settings import (
    DEATH_SOUND,
    SOUNDS_VOLUME,
    bullets,
    ENEMY_FIRE_DELAY,
    BULLET_TEXTURE,
    FIRE_SOUND,
)
from sprites.bullet import Bullet
from sprites.game_sprite import GameSprite, Movable


class Enemy(GameSprite, Movable):
    """
    Клас ворога.
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
        self.player_x = None
        self.player_y = None
        self.last_fire_time = pygame.time.get_ticks()  # Час останнього пострілу

    def fire(self) -> None:
        current_time = pygame.time.get_ticks()

        if current_time - self.last_fire_time >= ENEMY_FIRE_DELAY:
            sound = pygame.mixer.Sound(FIRE_SOUND)
            sound.set_volume(SOUNDS_VOLUME)
            sound.play()
            bullet = Bullet(
                BULLET_TEXTURE,
                self.rect.centerx,
                self.rect.centery,
                50,
                50,
                10,
                self.direction,
                40,
                "ENEMY",
            )
            bullets.add(bullet)
            self.last_fire_time = current_time  # Оновлюємо час останнього пострілу

    def move(self) -> None:
        if self.player_x and self.player_y:
            if self.rect.x < self.player_x:
                self.direction = "RIGHT"
                self.rect.x += self.speed
            elif self.rect.x > self.player_x:
                self.direction = "LEFT"
                self.rect.x -= self.speed

            if abs(self.rect.x - self.player_x) <= self.speed:
                if self.rect.y < self.player_y:
                    self.direction = "DOWN"
                    self.rect.y += self.speed
                elif self.rect.y > self.player_y:
                    self.direction = "UP"
                    self.rect.y -= self.speed

            self.rotate()

    def update(self, player_x: float, player_y: float) -> None:
        self.player_x, self.player_y = player_x, player_y
        self.move()
        self.fire()
        self.draw()

        if self.hp <= 0:
            sound = pygame.mixer.Sound(DEATH_SOUND)
            sound.set_volume(SOUNDS_VOLUME)
            sound.play()
            self.kill()
