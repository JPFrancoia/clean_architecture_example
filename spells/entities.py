from __future__ import annotations
from typing import NamedTuple

class Spell(NamedTuple):
    id: str
    name: str
    incantation: str | None
    effect: str
    canBeVerbal: bool | None
    type: str
    light: str
    creator: str | None

    @classmethod
    def from_dict(cls, data: dict) -> Spell:
        return cls(**data)

    def to_dict(self) -> dict:
        return self._asdict()
