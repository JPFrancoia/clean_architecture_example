from typing import Any
import requests

from .entities import Spell

# json data can't really be typed, but use this alias if you want to convey
# that some data is json
JSON = Any

BASE_URL = "https://wizard-world-api.herokuapp.com"


def fetch_spells_payload() -> JSON:
    req = requests.get(f"{BASE_URL}/Spells")

    # Avoid error handling boiler plate and crash if we don't get 200 back
    req.raise_for_status()

    return req.json()


def process_spells(payload: JSON) -> list[Spell]:
    return [Spell.from_dict(data) for data in payload]


def fetch_spells():
    return process_spells(fetch_spells_payload())


def fetch_spells2():
    req = requests.get(f"{BASE_URL}/Spells")

    # Avoid error handling boiler plate and crash if we don't get 200 back
    req.raise_for_status()

    [Spell.from_dict(data) for data in req.json()]


def test_process_spells():
    data = [
        {
            "id": "fbd3cb46-c174-4843-a07e-fd83545dce58",
            "name": "Opening Charm",
            "incantation": "Aberto",
            "effect": "Opens doors",
            "canBeVerbal": True,
            "type": "Charm",
            "light": "Blue",
            "creator": None,
        }
    ]

    target = [
        Spell(
            id="fbd3cb46-c174-4843-a07e-fd83545dce58",
            name="Opening Charm",
            incantation="Aberto",
            effect="Opens doors",
            canBeVerbal=True,
            type="Charm",
            light="Blue",
            creator=None,
        )
    ]

    assert process_spells(data) == target


if __name__ == "__main__":
    # fetch_spells()
    test_process_spells()
