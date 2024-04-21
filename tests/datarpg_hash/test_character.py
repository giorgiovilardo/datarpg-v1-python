from src.datarpg.datarpg_hash import character


def test_default_character() -> None:
    expected = {"health": 1000, "level": 1, "is_dead": False}
    assert all(kv in character.default() for kv in expected)


def test_characters_have_range() -> None:
    assert "range" in character.default()
