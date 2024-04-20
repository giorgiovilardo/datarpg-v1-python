import pytest

from src.datarpg import character
from src.datarpg.character import Character


def test_character_are_damaged_in_combat() -> None:
    char_1, char_2 = [character.Character(id=1), character.Character(id=2)]
    assert character.damage(char_1, char_2) == character.Character(
        id=2,
        health=999,
        level=1,
        is_dead=False,
    )


def test_character_can_die_in_combat() -> None:
    char_1 = character.Character(id=1)
    char_2 = character.Character(
        id=2,
        health=1,
        level=1,
        is_dead=False,
    )
    assert character.damage(char_1, char_2) == character.Character(
        id=2,
        health=0,
        level=1,
        is_dead=True,
    )


def test_dead_character_cant_be_healed() -> None:
    char_1 = character.Character(id=1)
    char_2 = character.Character(
        id=2,
        health=0,
        level=1,
        is_dead=True,
    )
    assert character.heal(char_1, char_2) == char_2


def test_alive_character_can_be_healed() -> None:
    char_1 = character.Character(id=1, health=1)
    assert character.heal(char_1, char_1) == character.Character(
        id=1,
        health=2,
        level=1,
        is_dead=False,
    )


def test_heal_cant_go_over_1000() -> None:
    char_1 = character.Character(id=1)
    char_2 = character.Character(id=2)
    assert character.heal(char_1, char_2) == char_2


def test_character_cant_damage_itself() -> None:
    char_1 = character.Character(id=1)
    assert character.damage(char_1, char_1) == char_1


def test_heal_cannot_heal_another() -> None:
    char_1 = character.Character(id=1)
    char_2 = character.Character(id=2)
    assert character.heal(char_1, char_2) == char_2


def test_scales_damage_down_if_attacker_5_levels_higher() -> None:
    char_1 = character.Character(id=1, level=6)
    char_2 = character.Character(id=2)
    assert character.damage(char_1, char_2) == character.Character(id=2, health=997)


def test_scales_damage_down_with_math_floor() -> None:
    char_1 = character.Character(id=1, level=7)
    char_2 = character.Character(id=2)
    assert character.damage(char_1, char_2) == character.Character(id=2, health=997)


def test_scales_damage_up_if_attacker_5_levels_lower() -> None:
    char_1 = character.Character(id=1, level=2)
    char_2 = character.Character(id=2, level=7)
    assert character.damage(char_1, char_2) == character.Character(
        id=2,
        health=997,
        level=7,
    )


def test_scales_damage_up_with_math_ceil() -> None:
    char_1 = character.Character(id=1)
    char_2 = character.Character(id=2, level=6)
    assert character.damage(char_1, char_2) == character.Character(
        id=2,
        health=998,
        level=6,
    )


@pytest.mark.parametrize(
    ("char_1", "char_2", "expected"),
    [
        (
            character.Character.melee(id=1),
            character.Character.ranged(id=2),
            character.Character.ranged(id=2),
        ),
        (
            character.Character.ranged(id=1),
            character.Character.melee(id=2),
            character.Character.melee(id=2, health=999),
        ),
        (
            character.Character.ranged(id=1),
            character.Character.ranged(id=2),
            character.Character.ranged(id=2, health=999),
        ),
        (
            character.Character.melee(id=1),
            character.Character.melee(id=2),
            character.Character.melee(id=2, health=999),
        ),
    ],
)
def test_character_must_be_in_range_to_damage(
    char_1: Character,
    char_2: Character,
    expected: Character,
) -> None:
    assert character.damage(char_1, char_2) == expected


def test_allies_cannot_damage_in_between_them() -> None:
    char_1 = Character.melee(id=1, factions=["t"])
    char_2 = Character.melee(id=2, factions=["t"])
    assert character.damage(char_1, char_2) == char_2


def test_allies_can_heal_in_between_them() -> None:
    char_1 = Character.melee(id=1, factions=["t"])
    char_2 = Character.melee(id=2, factions=["t"], health=1)
    assert character.heal(char_1, char_2) == Character.melee(
        id=2,
        factions=["t"],
        health=2,
    )
