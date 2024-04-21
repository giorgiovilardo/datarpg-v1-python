from src.datarpg.datarpg_hash import character


def test_default_character() -> None:
    expected = {"health": 1000, "level": 1, "is_dead": False}
    assert all(kv in character.default() for kv in expected)


def test_characters_have_range() -> None:
    assert character.default()["range"] == character.MELEE_RANGE
    assert character.default_ranged()["range"] == character.RANGED_RANGE


def test_characters_have_factions_but_start_with_none() -> None:
    assert not character.has_factions(character.default())
    assert not character.has_factions(character.default_ranged())


def test_characters_can_join_or_leave_factions() -> None:
    char = character.default()
    assert not character.has_factions(char)
    char = character.join_faction(char, "test_faction")
    assert character.has_factions(char)
    assert "test_faction" in char["factions"]
    char = character.leave_faction(char, "test_faction")
    assert not character.has_factions(char)
