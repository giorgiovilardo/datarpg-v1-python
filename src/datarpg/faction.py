import dataclasses
from typing import Any, ClassVar, Protocol


class HasFactions(Protocol):
    factions: list[str]
    __dataclass_fields__: ClassVar[dict[str, Any]]


def join(joiner: HasFactions, faction: str) -> HasFactions:
    return dataclasses.replace(joiner, factions=[*joiner.factions, faction])
