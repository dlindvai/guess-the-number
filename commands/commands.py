from . import commands


def _exec(context: dict, param: str):
    print('Zoznam použiteľných príkazov v hre:')
    for cmd in commands:
        print(f'* {cmd["name"]} - {cmd["description"]}')


cmd = {
    'name': 'prikazy',
    'description': 'zobrazí zoznam príkazov, ktoré sa dajú použiť v hre',
    'aliases': ('prikazy', 'commands', 'help', '?', 'cmd'),
    'exec': _exec
}
