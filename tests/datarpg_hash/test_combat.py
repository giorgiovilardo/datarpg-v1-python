from typing import Any, cast

from src.datarpg.datarpg_hash import character, combat
from src.datarpg.datarpg_hash.combat import Attacker, Defender, Healed, Healer


def _do_combat(
    *,
    attacker_opts: dict[str, Any] | None = None,
    defender_opts: dict[str, Any] | None = None,
) -> Defender:
    if attacker_opts is None:
        attacker_opts = {}
    if defender_opts is None:
        defender_opts = {}
    return combat.damage(
        cast(Attacker, character.default() | {"name": "attacker"} | attacker_opts),
        cast(Defender, character.default() | {"name": "defender"} | defender_opts),
    )


def test_damage() -> None:
    assert _do_combat()["health"] == 999


def test_damage_kills_if_health_goes_under_zero() -> None:
    second_combat = _do_combat(attacker_opts={"level": 2000})
    assert second_combat["health"] == 0
    assert second_combat["is_dead"] is True


def test_heal_can_heal_himself() -> None:
    char_1 = character.default()
    char_1.update({"health": 900})
    assert combat.heal(char_1, char_1)["health"] == 901


def test_heal_cannot_heal_if_dead() -> None:
    """Not correctly understood by pyright."""
    char_1 = cast(Healer, character.default() | {"is_dead": True})
    char_2 = cast(Healed, character.default() | {"is_dead": True})
    assert combat.heal(char_1, char_2) == char_2


def test_heal_health_cant_go_over_1000() -> None:
    """Not correctly understood by pyright."""
    char_1 = cast(Healer, character.default() | {"is_dead": True})
    char_2 = cast(Healed, character.default() | {"is_dead": True})
    assert combat.heal(char_1, char_2)["health"] == 1000


def test_heal_can_not_heal_other() -> None:
    char_1 = character.default()
    char_2 = cast(Healed, character.default() | {"health": 900, "name": "f"})
    assert combat.heal(char_1, char_2) == char_2


def test_same_char_cannot_hit_itself() -> None:
    char_1 = character.default()
    assert combat.damage(char_1, char_1) == char_1


def test_damage_is_increased_if_attacker_level_is_lower_than_defender() -> None:
    assert (
        _do_combat(attacker_opts={"level": 2}, defender_opts={"level": 100})["health"]
        == 997
    )


def test_damage_increased_rounds_up() -> None:
    assert _do_combat(defender_opts={"level": 100})["health"] == 998


def test_damage_is_decreased_if_attacker_level_is_higher_than_defender() -> None:
    assert _do_combat(attacker_opts={"level": 100})["health"] == 950


def test_damage_decreased_rounds_down() -> None:
    assert _do_combat(attacker_opts={"level": 7})["health"] == 997


def test_combat_allowed_only_if_attacker_in_range_of_defender() -> None:
    assert (
        _do_combat(attacker_opts={"range": 2}, defender_opts={"range": 20})["health"]
        == 1000
    )
    assert (
        _do_combat(attacker_opts={"range": 2}, defender_opts={"range": 2})["health"]
        == 999
    )
    assert (
        _do_combat(attacker_opts={"range": 20}, defender_opts={"range": 2})["health"]
        == 999
    )


def test_allies_cannot_fight() -> None:
    assert (
        _do_combat(
            attacker_opts={"factions": ["a"]}, defender_opts={"factions": ["a"]}
        )["health"]
        == 1000
    )


def test_allies_can_heal() -> None:
    char_1 = character.default()
    char_2 = cast(Healed, character.default() | {"health": 900, "name": "f"})
    assert combat.heal(char_1, char_2)["health"] == 901
