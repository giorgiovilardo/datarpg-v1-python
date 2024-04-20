from src.datarpg import faction
from src.datarpg.character import Character


def test_can_join_a_faction() -> None:
    char = Character.melee(id=1)
    assert faction.join(char, "TestFaction").factions == ["TestFaction"]
