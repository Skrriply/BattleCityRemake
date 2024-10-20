from typing import Tuple

from game import sprites
from game.settings import walls, enemies, ENEMY_TEXTURE, WALL_TEXTURE, PATH_TO_MAP
from game.utils import open_file


class MapObjectFactory:
    @staticmethod
    def create_wall(x: int, y: int) -> sprites.Wall:
        return sprites.Wall(WALL_TEXTURE, x * 100, y * 100, 100, 100)

    @staticmethod
    def create_enemy(x: int, y: int) -> sprites.Enemy:
        return sprites.Enemy(ENEMY_TEXTURE, x * 100, y * 100, 100, 100, 1)


class MapManager:
    OBJECT_MAP = {
        "#": MapObjectFactory.create_wall,
        "E": MapObjectFactory.create_enemy,
    }

    @staticmethod
    def load_map() -> Tuple[int, int]:
        file = open_file(PATH_TO_MAP)
        player_coords = (0, 0)

        for y, line in enumerate(file):
            for x, char in enumerate(line.strip()):
                if char in MapManager.OBJECT_MAP:
                    obj = MapManager.OBJECT_MAP[char](x, y)
                    if char == "#":
                        walls.add(obj)
                    elif char == "E":
                        enemies.add(obj)
                elif char == "P":  # Гравець
                    player_coords = (x * 100, y * 100)

        return player_coords
