from dataclasses import dataclass, field
from enum import StrEnum
from typing import Self


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
    ) -> Self:
        """Return a melee character with your options."""
        return cls(
            id=id,
            health=health,
            level=level,
            is_dead=is_dead,
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
    ) -> Self:
        """Return a melee character with your options."""
        return cls(
            id=id,
            health=health,
            level=level,
            is_dead=is_dead,
            role=Role.RANGED,
            range=20,
        )
