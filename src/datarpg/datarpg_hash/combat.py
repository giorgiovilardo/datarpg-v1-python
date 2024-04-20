from typing import TypedDict


class Attacker(TypedDict):
    level: int


class Liver(TypedDict):
    is_dead: bool


class HasHealth(TypedDict):
    health: int


class Defender(Liver, HasHealth):
    pass


def _new_health(attacker_power: int, defender_life: int) -> int:
    return max(defender_life - attacker_power, 0)


def damage(attacker: Attacker, defender: Defender) -> Defender:
    new_health = _new_health(attacker["level"], defender["health"])
    is_dead = new_health == 0
    return {**defender, "health": new_health, "is_dead": is_dead}
