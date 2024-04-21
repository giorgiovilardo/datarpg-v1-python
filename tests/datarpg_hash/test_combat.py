from collections.abc import Callable
from typing import Any

from src.datarpg.datarpg_hash import character, combat
from src.datarpg.datarpg_hash.combat import Defender


def _combat_between(
    *,
    char_1_opts: dict[str, Any] | None = None,
    char_2_opts: dict[str, Any] | None = None,
) -> Defender:
    return _call_fn_with_char_opts(combat.damage, char_1_opts, char_2_opts)


def _heal_between(
    *,
    char_1_opts: dict[str, Any] | None = None,
    char_2_opts: dict[str, Any] | None = None,
) -> Defender:
    return _call_fn_with_char_opts(combat.heal, char_1_opts, char_2_opts)


def _call_fn_with_char_opts(
    method: Callable[[Any, Any], Any],
    char_1_opts: dict[str, Any] | None = None,
    char_2_opts: dict[str, Any] | None = None,
) -> Defender:
    if char_1_opts is None:
        char_1_opts = {}
    if char_2_opts is None:
        char_2_opts = {}
    return method(
        character.default() | char_1_opts,
        character.default() | char_2_opts,
    )


def test_damage() -> None:
    assert _combat_between(char_1_opts={"name": "f"})["health"] == 999


def test_damage_can_kill_if_under_zero() -> None:
    second_combat = _combat_between(char_1_opts={"level": 2000, "name": "k"})
    assert second_combat["health"] == 0
    assert second_combat["is_dead"] is True


def test_heal_can_heal_himself() -> None:
    char_1 = character.default()
    char_1.update({"health": 900})
    assert combat.heal(char_1, char_1)["health"] == 901


def test_heal_cannot_heal_if_dead() -> None:
    char_1 = character.default()
    char_1.update({"is_dead": True})
    assert combat.heal(char_1, char_1) == char_1


def test_heal_health_cant_go_over_1000() -> None:
    char_1 = character.default()
    char_1.update({"level": 2000, "health": 900})
    assert combat.heal(char_1, char_1)["health"] == 1000


def test_heal_can_not_heal_other() -> None:
    char_1 = character.default()
    char_2 = character.default() | {"health": 900, "name": "f"}
    assert combat.heal(char_1, char_2) == char_2


def test_same_char_cannot_hit_itself() -> None:
    char_1 = character.default()
    assert combat.damage(char_1, char_1) == char_1


def test_damage_is_increased_if_attacker_level_is_lower_than_defender() -> None:
    assert (
        _combat_between(
            char_1_opts={"level": 2}, char_2_opts={"name": "m", "level": 100}
        )["health"]
        == 997
    )


def test_damage_increased_rounds_up() -> None:
    assert _combat_between(char_2_opts={"name": "m", "level": 100})["health"] == 998


def test_damage_is_decreased_if_attacker_level_is_higher_than_defender() -> None:
    assert _combat_between(char_1_opts={"name": "m", "level": 100})["health"] == 950


def test_damage_decreased_rounds_down() -> None:
    assert _combat_between(char_1_opts={"name": "m", "level": 7})["health"] == 997
