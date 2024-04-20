import dataclasses
from typing import Any, ClassVar, Protocol


class HasFactions(Protocol):
    __dataclass_fields__: ClassVar[dict[str, Any]]
    factions: list[str]


def join(joiner: HasFactions, faction: str) -> HasFactions:
    return dataclasses.replace(joiner, factions=[*joiner.factions, faction])


def leave(joiner: HasFactions, faction: str) -> HasFactions:
    return dataclasses.replace(
        joiner, factions=[f for f in joiner.factions if f != faction]
    )


def is_ally(member: HasFactions, other_member: HasFactions) -> bool:
    return any(f in member.factions for f in other_member.factions)
