import dataclasses
from dataclasses import dataclass
from typing import Any


@dataclass
class Prop:
    health: int = 1000
    is_destroyed: bool = False


def is_prop(a: Any) -> bool:
    return isinstance(a, Prop)


def damage(prop: Prop, damage: int) -> Prop:
    new_health = max(prop.health - damage, 0)
    new_is_destroyed = new_health == 0
    return dataclasses.replace(prop, health=new_health, is_destroyed=new_is_destroyed)
