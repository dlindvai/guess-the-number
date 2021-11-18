from helpers import get_item_by_name


def _exec(context: dict, param: str):
    backpack = context["backpack"]
    room = context["room"]
    name = param

    if not name:
        print("Neviem, čo chceš položiť na zem.")
        return

    item = get_item_by_name(name, backpack["items"])

    if item is None:
        print('Taký predmet sa v batohu nenachádza.')
        return

    backpack["items"].remove(item)
    room["items"].append(item)
    print(f'Predmet {name} si položil na zem.')


cmd = {
        'name': 'poloz',
        'description': 'vyberie predmet z batohu a položí ho na zem',
        'aliases': ('poloz', 'drop'),
        'exec': _exec
    },
