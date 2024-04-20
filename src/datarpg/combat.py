from typing import Any, ClassVar, Protocol, cast

from src.datarpg import character, prop
from src.datarpg.character import Character
from src.datarpg.prop import Prop, is_prop


class IsProp(Protocol):
    is_destroyed: bool


class IsCharacter(Protocol):
    level: int
    health: int


class HasHealth(Protocol):
    health: int


class CanFight(IsProp, IsCharacter, Protocol):
    __dataclass_fields__: ClassVar[dict[str, Any]]


def damage(attacker: CanFight, defender: CanFight) -> HasHealth:
    if is_prop(attacker):
        return defender
    if is_prop(defender):
        assert isinstance(defender, Prop)
        return prop.damage(defender, attacker.level)
    assert isinstance(attacker, Character)
    assert isinstance(defender, Character)
    return cast(HasHealth, character.damage(attacker, defender))


def heal(healer: CanFight, healed: CanFight) -> CanFight:
    if is_prop(healer) or is_prop(healed):
        return healed
    assert isinstance(healed, Character)
    assert isinstance(healer, Character)
    return cast(CanFight, character.heal(healer, healed))
