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


def test_characters_can_be_allies() -> None:
    char_1 = character.default()
    char_2 = character.default_ranged()
    char_1 = character.join_faction(char_1, "test_faction")
    char_2 = character.join_faction(char_2, "test_faction")
    assert character.are_allies(char_1, char_2)
    char_2 = character.leave_faction(char_2, "test_faction")
    assert not character.are_allies(char_1, char_2)
