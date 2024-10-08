import os
from typing import LiteralString

_WORK_DIR = os.path.dirname(__file__) + os.path.sep


def normalize_path(*args: str) -> LiteralString:
    return os.path.join(_WORK_DIR, *args)
