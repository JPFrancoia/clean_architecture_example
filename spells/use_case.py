from .data_registry import DataRegistry
from .entities import Spell
from .client import fetch_spells


class CollectSpellsUseCase:
    def __init__(self, data_registry: DataRegistry) -> None:
        self.reg = data_registry

    def run(self) -> None:
        spells = fetch_spells()
        self.reg.register_spells(spells)


if __name__ == "__main__":
    reg = DataRegistry("spells.json")
    use_case = CollectSpellsUseCase(reg)
    use_case.run()
