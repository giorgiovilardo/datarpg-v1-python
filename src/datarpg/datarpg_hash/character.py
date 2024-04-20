from typing import TypedDict


class Character(TypedDict):
    health: int
    level: int
    is_dead: bool


def default() -> Character:
    return {"health": 1000, "level": 1, "is_dead": False}
