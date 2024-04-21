import math
from typing import TypedDict

from src.datarpg.datarpg_hash import character


class Liver(TypedDict):
    is_dead: bool


class HasHealth(TypedDict):
    health: int


class HasName(TypedDict):
    name: str


class HasLevel(TypedDict):
    level: int


class HasRange(TypedDict):
    range: int


class Attacker(HasName, HasLevel, HasRange):
    pass


class Defender(Liver, HasHealth, HasName, HasLevel, HasRange):
    pass


def _calculate_attack_power(
    attacker_level: int,
    defender_level: int,
    level_threshold: int = 5,
    power_multiplier: int = 2,
) -> int:
    match attacker_level - defender_level:
        case diff if diff >= level_threshold:
            return attacker_level // power_multiplier
        case diff if abs(diff) >= level_threshold:
            return attacker_level + math.ceil(attacker_level / power_multiplier)
        case _:
            return attacker_level


def _calculate_new_life_stats(
    defender_health: int,
    attacker_power: int,
) -> tuple[int, bool]:
    new_health = max(defender_health - attacker_power, 0)
    is_dead = new_health <= 0
    return new_health, is_dead


def _is_attack_forbidden(attacker: Attacker, defender: Defender) -> bool:
    if character.is_the_same(attacker, defender):
        return True
    if attacker["range"] < defender["range"]:
        return True
    return False


def damage(attacker: Attacker, defender: Defender) -> Defender:
    # public function, should be properly validated
    # but for the moment is typechecked
    if _is_attack_forbidden(attacker, defender):
        return defender
    attacker_power = _calculate_attack_power(attacker["level"], defender["level"])
    new_health, is_dead = _calculate_new_life_stats(defender["health"], attacker_power)
    return {
        **defender,
        "health": new_health,
        "is_dead": is_dead,
        "name": defender["name"],
        "level": defender["level"],
        "range": defender["range"],
    }


class Healer(Liver, HasLevel, HasHealth, HasName):
    pass


class Healed(Liver, HasHealth, HasName):
    pass


def _can_be_healed(healer: Healer, healed: Healed) -> bool:
    if healer["is_dead"]:
        return False
    if not character.is_the_same(healer, healed):
        return False
    return True


def heal(healer: Healer, healed: Healed) -> Healed:
    # public function, should be properly validated
    # but for the moment is typechecked
    if not _can_be_healed(healer, healed):
        return healed
    new_health = min(healer["level"] + healer["health"], 1000)
    return {
        **healed,
        "health": new_health,
        "is_dead": healer["is_dead"],
        "name": healer["name"],
    }
