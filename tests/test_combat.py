from typing import cast

from src.datarpg import character, combat, prop
from src.datarpg.combat import CanFight


def test_prop_v_prop_does_nothing() -> None:
    prop_1 = cast(CanFight, prop.Prop())
    prop_2 = cast(CanFight, prop.Prop(health=300))
    assert combat.damage(prop_1, prop_2) == prop_2
    assert combat.damage(prop_2, prop_1) == prop_1


def test_prop_cant_damage_character() -> None:
    p = cast(CanFight, prop.Prop())
    c = cast(CanFight, character.Character.melee(id=1))
    cr = cast(CanFight, character.Character.ranged(id=1))
    assert combat.damage(p, c) == c
    assert combat.damage(p, cr) == cr


def test_prop_in_heal_does_nothing() -> None:
    c = cast(CanFight, character.Character.melee(id=1))
    p = cast(CanFight, prop.Prop(health=300))
    assert combat.heal(c, p) == p
    assert combat.heal(p, c) == c


def test_prop_can_be_damaged_by_characters() -> None:
    p = cast(CanFight, prop.Prop())
    pr = cast(CanFight, prop.Prop())
    c = cast(CanFight, character.Character.melee(id=1))
    cr = cast(CanFight, character.Character.ranged(id=1))
    assert combat.damage(c, p) == cast(CanFight, prop.Prop(health=999))
    assert combat.damage(cr, pr) == cast(CanFight, prop.Prop(health=999))
