from typing import cast

import pytest

from src.datarpg import faction
from src.datarpg.character import Character
from src.datarpg.faction import HasFactions


def test_can_join_a_faction() -> None:
    char: HasFactions = cast(HasFactions, Character.melee(id=1))
    assert faction.join(char, "TestFaction").factions == ["TestFaction"]


def test_can_leave_a_faction() -> None:
    char: HasFactions = cast(HasFactions, Character.melee(id=1))
    assert faction.join(char, "TestFaction").factions == ["TestFaction"]
    assert faction.leave(char, "TestFaction").factions == []


@pytest.mark.parametrize(
    ("char_1", "char_2", "expected"),
    [
        (Character.melee(id=1), Character.ranged(id=2), True),
    ],
)
def test_can_spot_alliances(
    *,
    char_1: HasFactions,
    char_2: HasFactions,
    expected: bool,
) -> None:
    char_1 = faction.join(char_1, "TestFaction")
    char_2 = faction.join(char_2, "TestFaction")
    assert faction.is_ally(char_1, char_2) is expected
