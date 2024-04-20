from src.datarpg.datarpg_hash import character, combat


def test_damage() -> None:
    char_1 = character.default()
    char_1.update({"name": "foffo"})
    char_2 = character.default()
    assert combat.damage(char_1, char_2) == {
        "name": "",
        "health": 999,
        "level": 1,
        "is_dead": False,
    }


def test_damage_ez_test_ez_life() -> None:
    assert combat.damage(
        {"level": 2, "name": "foffo"},
        {"health": 1000, "is_dead": False, "name": "faffo", "level": 2},
    ) == {
        "name": "faffo",
        "health": 998,
        "is_dead": False,
        "level": 2,
    }
    assert combat.damage(
        {"level": 2000, "name": "foffo"},
        {"name": "faffo", "health": 1000, "is_dead": True, "level": 2},
    ) == {
        "name": "faffo",
        "health": 0,
        "is_dead": True,
        "level": 2,
    }


def test_heal_can_heal_himself() -> None:
    char_1 = character.default()
    char_1.update({"health": 900})
    assert combat.heal(char_1, char_1) == {
        "health": 901,
        "is_dead": False,
        "level": 1,
        "name": "",
    }


def test_heal_cannot_heal_if_dead() -> None:
    char_1 = character.default()
    char_1.update({"is_dead": True})
    assert combat.heal(char_1, char_1) == char_1


def test_heal_health_cant_go_over_1000() -> None:
    char_1 = character.default()
    char_1.update({"level": 2000, "health": 900})
    assert combat.heal(char_1, char_1) == {
        "health": 1000,
        "is_dead": False,
        "level": 2000,
        "name": "",
    }


def test_heal_can_not_heal_other() -> None:
    char_1 = character.default()
    char_2 = character.default()
    char_2.update({"health": 900, "name": "f"})
    assert combat.heal(char_1, char_2) == char_2


def test_same_char_cannot_hit_itself() -> None:
    char_1 = character.default()
    assert combat.damage(char_1, char_1) == char_1


def test_damage_is_increased_if_attacker_level_is_lower_than_defender() -> None:
    char_1 = character.default()
    char_1.update({"name": "mastro", "level": 2})
    char_2 = character.default()
    char_2.update({"level": 100})
    assert combat.damage(char_1, char_2) == {
        "name": "",
        "health": 997,
        "level": 100,
        "is_dead": False,
    }


def test_damage_increased_rounds_up() -> None:
    char_1 = character.default()
    char_1.update({"name": "mastro"})
    char_2 = character.default()
    char_2.update({"level": 100})
    assert combat.damage(char_1, char_2) == {
        "name": "",
        "health": 998,
        "level": 100,
        "is_dead": False,
    }


def test_damage_is_decreased_if_attacker_level_is_higher_than_defender() -> None:
    char_1 = character.default()
    char_1.update({"name": "mastro", "level": 100})
    char_2 = character.default()
    assert combat.damage(char_1, char_2) == {
        "name": "",
        "health": 950,
        "level": 1,
        "is_dead": False,
    }


def test_damage_decreased_rounds_down() -> None:
    char_1 = character.default()
    char_1.update({"name": "mastro", "level": 7})
    char_2 = character.default()
    assert combat.damage(char_1, char_2) == {
        "name": "",
        "health": 997,
        "level": 1,
        "is_dead": False,
    }
