#!/usr/bin/env python3
from typing import Dict
import states
from items import figa, coin, canister, matches, fire_extinguisher, newspaper, door
from commands import intro_banner, about_game, commands_list, show_inventory, take_item, drop_item, quit_game, \
    inspect_item, look_around

if __name__ == '__main__':
    # init game
    context = {
        'state': states.PLAY,
        'backpack': {
            'items': [],
            'max': 2
        },
        'world': {},
        'room': {}
    }

    context['backpack']['items'].append(figa)
    context['backpack']['items'].append(coin)

    context['room'] = {
        'name': 'Dungeon',
        'description': 'Nachádzaš sa v tmavej zatuchnutej miestnosti. Na kamenných stenách sa nenachádza žiadne okno, '
                       'čo dáva tušiť, \nže si niekoľko metrov pod zemou. Žeby košický hrad? Aj to je možné, '
                       'ti prebleslo hlavou.',
        'items': [canister, matches, newspaper, fire_extinguisher, door],
        'exits': []
    }

    intro_banner()
    look_around(context)

    # main loop
    while context['state'] == states.PLAY:
        line = input('> ').lower().strip()
        if line == '':
            continue

        elif line in ('koniec', 'quit', 'q', 'bye', 'end'):
            quit_game(context)

        elif line in ('o hre', 'about', 'info'):
            about_game(context)

        elif line in ('prikazy', 'commands', 'help', '?', 'cmd'):
            commands_list(context)

        elif line in ('rozhliadni sa', 'look around', 'show room'):
            look_around(context)

        elif line in ('inventory', 'i', 'batoh', 'backpack'):
            show_inventory(context)

        elif line.startswith('vezmi'):
            take_item(line, context)

        elif line.startswith('poloz'):
            drop_item(line, context)

        elif line.startswith('preskumaj'):
            inspect_item(line, context)

        else:
            print('Taký príkaz nepoznám.')

    print('Dúfame, že ste si hru užili! Dovidienia!!')
    print('(c)2021 by Dárius Lindvai')
