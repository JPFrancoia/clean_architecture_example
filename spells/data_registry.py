from typing import Iterable

from tinydb import TinyDB

from .entities import Spell

class DataRegistry:

    def __init__(self, db_path: str) -> None:
        self.db = TinyDB(db_path)

    def register_spell(self, spell: Spell) -> None:
        table = self.db.table("spells")
        table.insert(spell.to_dict())

    def register_spells(self, spells: Iterable[Spell]) -> None:
        table = self.db.table("spells")
        table.insert_multiple([spell.to_dict() for spell in spells])

    def fetch_spells(self) -> list[Spell]:
        table = self.db.table("spells")
        return [Spell.from_dict(doc) for doc in table.all()]
