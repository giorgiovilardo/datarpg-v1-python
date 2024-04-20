from src.datarpg import character


def test_default_character() -> None:
    assert character.Character(id=1) == character.Character(
        id=1,
        health=1000,
        level=1,
        is_dead=False,
    )
