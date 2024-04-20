from src.datarpg.datarpg_hash import character, combat


def test_damage() -> None:
    char_1 = character.default()
    char_2 = character.default()
    assert combat.damage(char_1, char_2) == {
        "health": 999,
        "level": 1,
        "is_dead": False,
    }


def test_damage_ez_test_ez_life() -> None:
    assert combat.damage({"level": 2}, {"health": 1000, "is_dead": True}) == {
        "health": 998,
        "is_dead": False,
    }
    assert combat.damage({"level": 2000}, {"health": 1000, "is_dead": True}) == {
        "health": 0,
        "is_dead": True,
    }
