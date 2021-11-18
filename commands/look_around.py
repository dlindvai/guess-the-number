from helpers import show_room


def _exec(context: dict, param: str):
    show_room(context["room"])


cmd = {
    'name': 'rozhliadni sa',
    'description': 'zobrazí názov a opis aktuálnej miestnosti',
    'aliases': ('rozhliadni sa', 'look around', 'show room'),
    'exec': _exec
}
