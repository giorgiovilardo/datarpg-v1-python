from typing import TypedDict


class HasName(TypedDict):
    name: str


class HasFactions(TypedDict):
    factions: list[str]


class Character(HasName, HasFactions):
    health: int
    level: int
    is_dead: bool
    range: int


MELEE_RANGE = 2
RANGED_RANGE = 20


def default() -> Character:
    return {
        "name": "",
        "health": 1000,
        "level": 1,
        "is_dead": False,
        "range": MELEE_RANGE,
        "factions": [],
    }


def default_ranged() -> Character:
    return {
        "name": "",
        "health": 1000,
        "level": 1,
        "is_dead": False,
        "range": RANGED_RANGE,
        "factions": [],
    }


def is_the_same(a: HasName, b: HasName) -> bool:
    # public function, should be validated
    return a["name"] == b["name"]


def has_factions(char: HasFactions) -> bool:
    return len(char["factions"]) > 0


def join_faction(char: HasFactions, faction: str) -> HasFactions:
    new_factions = (
        char["factions"] + [faction]
        if faction not in char["factions"]
        else char["factions"]
    )
    return char | {"factions": new_factions}


def leave_faction(char: HasFactions, faction: str) -> HasFactions:
    new_factions = [f for f in char["factions"] if f != faction]
    return char | {"factions": new_factions}
