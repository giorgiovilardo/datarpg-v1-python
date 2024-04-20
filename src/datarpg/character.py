import dataclasses
import math
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Self, cast

from src.datarpg.faction import HasFactions, is_ally


class Role(StrEnum):
    MELEE = "melee"
    RANGED = "ranged"


@dataclass(kw_only=True)
class Character:
    id: int
    health: int = 1000
    level: int = 1
    is_dead: bool = False
    role: Role = Role.MELEE
    range: int = 2
    factions: list[str] = field(default_factory=list)

    @classmethod
    def melee(
        cls: type[Self],
        *,
        id: int,
        health: int = 1000,
        level: int = 1,
        is_dead: bool = False,
        factions: list[str] | None = None,
    ) -> Self:
        """Return a melee character with your options."""
        if factions is None:
            factions = []
        return cls(
            id=id,
            health=health,
            level=level,
            is_dead=is_dead,
            factions=factions,
            role=Role.MELEE,
            range=2,
        )

    @classmethod
    def ranged(
        cls: type[Self],
        *,
        id: int,
        health: int = 1000,
        level: int = 1,
        is_dead: bool = False,
        factions: list[str] | None = None,
    ) -> Self:
        """Return a melee character with your options."""
        if factions is None:
            factions = []
        return cls(
            id=id,
            health=health,
            level=level,
            is_dead=is_dead,
            factions=factions,
            role=Role.RANGED,
            range=20,
        )


def damage(attacker: Character, defender: Character) -> Character:
    damage_variation_threshold = 5

    def _calculate_damage(a: Character, d: Character) -> int:
        if a.level - d.level >= damage_variation_threshold:
            return a.level // 2
        if d.level - a.level >= damage_variation_threshold:
            return math.ceil(a.level * 1.5)
        return a.level

    if attacker.range < defender.range:
        return defender
    if attacker.id == defender.id:
        return attacker
    if is_ally(attacker, defender):
        return defender
    _damage = _calculate_damage(attacker, defender)
    new_health = max(defender.health - _damage, 0)
    is_dead = new_health == 0
    return dataclasses.replace(defender, health=new_health, is_dead=is_dead)


def heal(healer: Character, healed: Character) -> Character:
    if healer.id != healed.id and not is_ally(
        cast(HasFactions, healer), cast(HasFactions, healed)
    ):
        return healed
    return dataclasses.replace(healed, health=min(healer.level + healed.health, 1000))
