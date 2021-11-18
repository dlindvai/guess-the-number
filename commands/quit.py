import states


def _exec(context: dict, param: str):
    context["state"] = states.QUIT


cmd = {
    'name': 'koniec',
    'description': 'ukončí hru',
    'aliases': ('koniec', 'quit', 'q', 'bye', 'end'),
    'exec': _exec
}
