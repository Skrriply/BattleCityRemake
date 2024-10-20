import json
import os
from typing import LiteralString, Union, Any, Dict, List

_WORK_DIR = os.path.dirname(__file__) + os.path.sep


def normalize_path(*args: str) -> LiteralString:
    return os.path.join(_WORK_DIR, *args)


def open_file(
    path_to_file: str, is_json: bool = False
) -> Union[List[str], Dict[str, Any]]:
    with open(path_to_file, "r", encoding="utf-8") as file:
        if is_json:
            return json.load(file)
        return file.readlines()
