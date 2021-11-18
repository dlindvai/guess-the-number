from helpers import get_item_by_name


def _exec(context: dict, param: str):
    name = param
    if not name:
        print("Neviem, aký predmet chceš preskúmať.")
        return

    item = get_item_by_name(name, context["backpack"]["items"] + context["room"]["items"])

    if item is None:
        print('Taký predmet sa nikde nenachádza.')
        return

    print(item["description"])


cmd = {
    'name': 'preskumaj',
    'description': 'vypíše vlastnosť daného predmetu',
    'aliases': ('preskumaj', 'examine'),
    'exec': _exec
}
