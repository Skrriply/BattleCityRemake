import sys

import pygame

import sprites as sprites
from map import MapManager
from settings import (
    PLAYER_TEXTURE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    window,
    clock,
    FPS,
    BACKGROUND_TEXTURE,
    BACKGROUND_MUSIC,
    enemies,
    screen_manager,
    COLORS,
    walls,
    END_TEXTURE,
    bullets,
    sound_manager,
    medkits
)

# Змінення заголовка й іконки вікна
pygame.display.set_caption("Battle City Remake")
pygame.display.set_icon(pygame.image.load(PLAYER_TEXTURE))

# Музика
background_music = pygame.mixer.Sound(BACKGROUND_MUSIC)
background_music.set_volume(0.05)
background_music.play(-1)


class Game:
    def __init__(self) -> None:
        self.map_manager = MapManager()
        self._create_sprites()

    def _create_sprites(self) -> None:
        # Створення кнопок
        callbacks = sprites.ButtonCallbacks()
        self.start_button = sprites.Button(
            WINDOW_WIDTH / 2,
            450,
            170,
            50,
            "Start",
            COLORS["green"],
            callbacks.start_game,
        )
        self.continue_button = sprites.Button(
            WINDOW_WIDTH / 2,
            450,
            170,
            50,
            "Continue",
            COLORS["green"],
            callbacks.start_game,
        )
        self.exit_button = sprites.Button(
            WINDOW_WIDTH / 2,
            510,
            170,
            50,
            "Exit",
            COLORS["red"],
            callbacks.exit
        )
        self.retry_button = sprites.Button(
            WINDOW_WIDTH / 2,
            450,
            170,
            50,
            "Retry",
            COLORS["yellow"],
            self.restart
        )

        # Створення гравця та мапи
        player_x, player_y = self.map_manager.load_map()
        self.player = sprites.Player(
            PLAYER_TEXTURE, player_x, player_y, 85, 100, 5, 120
        )


    @staticmethod
    def _handle_events() -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screen = screen_manager.screen
                    if screen == "GAME":
                        screen_manager.change_screen("PAUSE")
                    elif screen == "PAUSE" and screen not in ["MENU", "END"]:
                        screen_manager.change_screen("GAME")

    def _check_collisions(self) -> None:
        player_bullets = [bullet for bullet in bullets if bullet.owned_by == "PLAYER"]
        enemy_bullets = [bullet for bullet in bullets if bullet.owned_by == "ENEMY"]

        # Взаємодія ворога із кулями
        for bullet in player_bullets:
            collided_enemies = pygame.sprite.spritecollide(bullet, enemies, False)
            if collided_enemies:
                sound_manager.play_sound("hit")
                bullet.kill()
                for enemy in collided_enemies:
                    enemy.hp -= bullet.damage

        # Взаємодія гравця із кулями
        for bullet in enemy_bullets:
            collided = pygame.sprite.spritecollide(bullet, [self.player], False)
            if collided:
                sound_manager.play_sound("hit")
                bullet.kill()
                self.player.hp -= bullet.damage

        # Взаємодія стіни із кулями
        for bullet in bullets:
            collided_walls = pygame.sprite.spritecollide(bullet, walls, False)
            if collided_walls:
                sound_manager.play_sound("wall_hit")
                bullet.kill()
                for wall in collided_walls:
                    wall.hp -= bullet.damage

        # Взаємодія ворога з гравцем
        for enemy in enemies:
            collided = pygame.sprite.spritecollide(enemy, [self.player], False)
            if collided:
                sound_manager.play_sound("death")
                self.player.hp = 0

        # Взаємодія аптечки з гравцем
        for medkit in medkits:
            collided = pygame.sprite.spritecollide(medkit, [self.player], False)
            if collided:
                medkit.kill()
                self.player.hp += medkit.heal

    def _game_update(self) -> None:
        window.fill(COLORS["black"])
        medkits.update()
        walls.update()
        bullets.update()
        enemies.update(self.player.rect.x, self.player.rect.y)
        self.player.update()
        self._check_collisions()

    def _menu_update(self) -> None:
        window.blit(
            pygame.transform.scale(
                pygame.image.load(BACKGROUND_TEXTURE), (WINDOW_WIDTH, WINDOW_HEIGHT)
            ),
            (0, 0),
        )
        self.start_button.update()
        self.exit_button.update()

    def _end_update(self) -> None:
        window.blit(
            pygame.transform.scale(
                pygame.image.load(END_TEXTURE), (WINDOW_WIDTH, WINDOW_HEIGHT)
            ),
            (0, 0),
        )
        self.retry_button.update()
        self.exit_button.update()

    def _pause_update(self) -> None:
        self.continue_button.update()
        self.exit_button.update()

    def _update_screen(self) -> None:
        window.fill(COLORS["black"])
        if screen_manager.screen == "MENU":
            self._menu_update()
        elif screen_manager.screen == "GAME":
            self._game_update()
        elif screen_manager.screen == "END":
            self._end_update()
        elif screen_manager.screen == "PAUSE":
            self._pause_update()

        pygame.display.update()
        clock.tick(FPS)

    def restart(self) -> None:
        self.player.kill()
        enemies.empty()
        game._create_sprites()
        screen_manager.change_screen("GAME")

    def start(self) -> None:
        while True:
            self._handle_events()
            self._update_screen()


if __name__ == "__main__":
    game = Game()
    game.start()
