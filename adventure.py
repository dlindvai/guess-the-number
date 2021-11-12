#!/usr/bin/env python3
from typing import Dict
import states

from commands import intro_banner, about_game, commands_list, show_inventory, take_item, drop_item, quit_game,\
    inspect_item
from items import figa, coin, canister, matches, fire_extinguisher, newspaper, door


def show_room(room: Dict):
    """
    Show content of the room.
    The function shows name and description of the room. It also prints the list of items, which are in the room, or
    the information about there are no items in the room. Finally, it prints out also list of available exits from the
    room or special string, when there is no exit from the room.
    :param room: the room to print info about
    """

    if type(room) is not dict:
        raise TypeError('Room is not of type "Dictionary"')

    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(f'{room["description"]}')

    if not room["items"]:
        print('V miestnosti sa nenáchadzajú žiadne predmety.')
    else:
        print('V miestnosti vidíš tieto predmety:')
        for item in room["items"]:
            print(f'* {item["name"]}')
        # print(f'Vidis: {", ".join(room["items"])}')

    if not room["exits"]:
        print('Z miestnosti nevedú žiadne východy.')
    else:
        print('Z miestnosti sa vieš dostať von týmito východmi:')
        for out in room["exits"]:
            print(f'* {out}')


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
    show_room(context["room"])

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
            show_room(context['room'])

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
