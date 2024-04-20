import math
from typing import TypedDict


class Liver(TypedDict):
    is_dead: bool


class HasHealth(TypedDict):
    health: int


class HasName(TypedDict):
    name: str


class HasLevel(TypedDict):
    level: int


class Attacker(HasName, HasLevel):
    pass


class Defender(Liver, HasHealth, HasName, HasLevel):
    pass


def _calculate_attack_power(
    attacker_level: int,
    defender_level: int,
) -> int:
    threshold = 5
    if attacker_level - defender_level >= threshold:
        return attacker_level // 2
    if defender_level - attacker_level >= threshold:
        return attacker_level + math.ceil(attacker_level / 2)
    return attacker_level


def damage(attacker: Attacker, defender: Defender) -> Defender:
    if attacker["name"] == defender["name"]:
        return defender
    attacker_power = _calculate_attack_power(attacker["level"], defender["level"])
    new_health = max(defender["health"] - attacker_power, 0)
    is_dead = new_health == 0
    return {
        **defender,
        "health": new_health,
        "is_dead": is_dead,
        "name": defender["name"],
        "level": defender["level"],
    }


class Healer(Liver, HasLevel, HasHealth, HasName):
    pass


class Healed(Liver, HasHealth, HasName):
    pass


def heal(healer: Healer, healed: Healed) -> Healed:
    if healer["is_dead"] or healer["name"] != healed["name"]:
        return healed
    new_health = min(healer["level"] + healer["health"], 1000)
    return {
        **healed,
        "health": new_health,
        "is_dead": healer["is_dead"],
        "name": healer["name"],
    }
