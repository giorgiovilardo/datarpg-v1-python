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


class Defender(Liver, HasHealth, HasName):
    pass


def _new_health(attacker_power: int, defender_life: int) -> int:
    return max(defender_life - attacker_power, 0)


def damage(attacker: Attacker, defender: Defender) -> Defender:
    if attacker["name"] == defender["name"]:
        return defender
    new_health = _new_health(attacker["level"], defender["health"])
    is_dead = new_health == 0
    return {
        **defender,
        "health": new_health,
        "is_dead": is_dead,
        "name": defender["name"],
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
