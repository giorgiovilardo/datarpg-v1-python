from src.datarpg import character
from src.datarpg.character import Role


def test_default_melee_character() -> None:
    assert character.Character.melee(id=1) == character.Character(
        id=1,
        health=1000,
        level=1,
        is_dead=False,
        role=Role.MELEE,
        range=2,
    )


def test_default_character() -> None:
    assert character.Character.ranged(id=1) == character.Character(
        id=1,
        health=1000,
        level=1,
        is_dead=False,
        role=Role.RANGED,
        range=20,
    )
