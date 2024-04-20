from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Self


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

    @classmethod
    def melee(cls: Self, **kwargs: dict[str, Any]) -> Self:
        """Return a melee character with your options."""
        return cls(**kwargs, role=Role.MELEE, range=2)

    @classmethod
    def ranged(cls: Self, **kwargs: dict[str, Any]) -> Self:
        """Return a ranged character with your options."""
        return cls(**kwargs, role=Role.RANGED, range=20)
