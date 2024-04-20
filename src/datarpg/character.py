from dataclasses import dataclass


@dataclass(kw_only=True)
class Character:
    id: int
    health: int = 1000
    level: int = 1
    is_dead: bool = False
