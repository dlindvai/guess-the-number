from helpers import get_item_by_name
from items import MOVABLE


def _exec(context: dict, param: str):
    backpack = context["backpack"]
    room = context["room"]
    name = param
    if not name:
        print("Neviem, čo chceš zobrať.")
        return

    item = get_item_by_name(name, room["items"])

    if item is None:
        print('Taký predmet tu nikde nevidím.')
        return

    if MOVABLE not in item["features"]:
        print('Tento predmet sa nedá vziať.')
        return

    if len(backpack["items"]) >= backpack["max"]:
        print('Batoh je plný')
        return

    room["items"].remove(item)
    backpack["items"].append(item)
    print(f'Predmet {name} si si vložil do batohu.')


cmd = {
    'name': 'vezmi',
    'description': 'vezme predmet z miestnosti a vloží ho do batohu',
    'aliases': ('vezmi',),
    'exec': _exec
}
