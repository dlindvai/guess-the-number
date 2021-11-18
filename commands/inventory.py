def _exec(context: dict, param: str):
    if not context["backpack"]["items"]:
        print('Tvoj batoh je prázdny.')
    else:
        print('V batohu máš:')
        for item in context["backpack"]["items"]:
            print(f'    * {item["name"]}')


cmd = {
    'name': 'inventar',
    'description': 'zobrazí obsah inventára',
    'aliases': ('inventory', 'i', 'batoh', 'backpack'),
    'exec': _exec
},
