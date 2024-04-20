import dataclasses
import math
from typing import Protocol

DAMAGE_VARIATION_THRESHOLD = 5


class Identifiable(Protocol):
    id: int


class Damageable(Protocol):
    level: int
    health: int


class Liveable(Protocol):
    is_dead: bool


class Rangeable(Protocol):
    range: int


class CanFight(Liveable, Damageable, Identifiable, Rangeable, Protocol):
    pass


def _calculate_damage(attacker: Damageable, defender: Damageable) -> int:
    if attacker.level - defender.level >= DAMAGE_VARIATION_THRESHOLD:
        return attacker.level // 2
    if defender.level - attacker.level >= DAMAGE_VARIATION_THRESHOLD:
        return math.ceil(attacker.level * 1.5)
    return attacker.level


def damage(attacker: CanFight, defender: CanFight) -> CanFight:
    if attacker.range < defender.range:
        return defender
    if attacker.id == defender.id:
        return attacker
    _damage = _calculate_damage(attacker, defender)
    new_health = max(defender.health - _damage, 0)
    is_dead = new_health == 0
    return dataclasses.replace(defender, health=new_health, is_dead=is_dead)


def heal(healer: CanFight, healed: CanFight) -> CanFight:
    if healed.is_dead:
        return healed
    if healer.id != healed.id:
        return healed
    return dataclasses.replace(healed, health=min(healer.level + healed.health, 1000))
