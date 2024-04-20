from src.datarpg import character, combat


def test_character_are_damaged_in_combat() -> None:
    char_1, char_2 = [character.Character(id=1), character.Character(id=2)]
    assert combat.damage(char_1, char_2) == character.Character(
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
    assert combat.damage(char_1, char_2) == character.Character(
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
    assert combat.heal(char_1, char_2) == char_2


def test_alive_character_can_be_healed() -> None:
    char_1 = character.Character(id=1, health=1)
    assert combat.heal(char_1, char_1) == character.Character(
        id=1,
        health=2,
        level=1,
        is_dead=False,
    )


def test_heal_cant_go_over_1000() -> None:
    char_1 = character.Character(id=1)
    char_2 = character.Character(id=2)
    assert combat.heal(char_1, char_2) == char_2


def test_character_cant_damage_itself() -> None:
    char_1 = character.Character(id=1)
    assert combat.damage(char_1, char_1) == char_1


def test_heal_cannot_heal_another() -> None:
    char_1 = character.Character(id=1)
    char_2 = character.Character(id=2)
    assert combat.heal(char_1, char_2) == char_2


def test_scales_damage_down_if_attacker_5_levels_higher() -> None:
    char_1 = character.Character(id=1, level=6)
    char_2 = character.Character(id=2)
    assert combat.damage(char_1, char_2) == character.Character(id=2, health=997)


def test_scales_damage_down_with_math_floor() -> None:
    char_1 = character.Character(id=1, level=7)
    char_2 = character.Character(id=2)
    assert combat.damage(char_1, char_2) == character.Character(id=2, health=997)


def test_scales_damage_up_if_attacker_5_levels_lower() -> None:
    char_1 = character.Character(id=1, level=2)
    char_2 = character.Character(id=2, level=7)
    assert combat.damage(char_1, char_2) == character.Character(
        id=2,
        health=997,
        level=7,
    )


def test_scales_damage_up_with_math_ceil() -> None:
    char_1 = character.Character(id=1)
    char_2 = character.Character(id=2, level=6)
    assert combat.damage(char_1, char_2) == character.Character(
        id=2,
        health=998,
        level=6,
    )
