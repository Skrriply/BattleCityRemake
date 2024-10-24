import pygame
from settings import bullets, ENEMY_FIRE_DELAY, BULLET_TEXTURE, sound_manager, walls
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
                "ENEMY",
            )
            bullets.add(bullet)
            self.last_fire_time = current_time  # Оновлюємо час останнього пострілу

    def move(self) -> None:
        previous_coords = self.rect.copy()

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

        if pygame.sprite.spritecollide(self, walls, False):
            self.rect = previous_coords

        self.rotate()

    def update(self, player_x: float, player_y: float) -> None:
        self.player_x, self.player_y = player_x, player_y
        self.move()
        self.fire()
        self.draw()

        if self.hp <= 0:
            sound_manager.play_sound("death")
            self.kill()
