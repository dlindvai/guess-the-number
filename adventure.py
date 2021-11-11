#!/usr/bin/env python3
import states


def intro_banner():
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print("|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/")
    print("                       and his Great Escape                        ")
    print()


def about_game():
    print('Túto hru, inšpirovanú slávnym Indiana Jonesom, vytvoril začínajúci vývojár Darius Lindvai.')
    print('Na začiatku hry sa ocitnete v roli Indiana Jonesa, ktorý sa snaží uniknúť z uzamknutej miestnosti.')
    print('Vašou úlohou je preskúmať miestnosť a nájsť všetky stopy a predmety, ktoré vám pri úniku pomôžu.')


def commands_list():
    print('Zoznam pouzitelnych prikazov v hre:')
    print('* koniec/quit/q/bye/end - ukonci hru')
    print('* o hre/about/info - zobrazi zakladne informacie o hre')
    print('* prikazy/commands/help/? - zobrazi zoznam prikazov')
    print('* rozhliadni sa/look around/show room - zobrazi nazov a opis aktualnej miestnosti')
    print('* inventory/i/batoh/backpack - zobrazi obsah inventara')


def show_room(room: dict):
    """
    Show content of the room.
    The function shows name and description of the room. It also prints the list of items, which are in the room, or
    the information about there are no items in the room. Finally, it prints out also list of available exits from the
    room or special string, when there is no exit from the room.
    :param room: the room to print info about
    """

    if type(room) is not dict:
        raise TypeError('Room is not of type "Dictionary"')

    print(f'Nachadzas sa v miestnosti {room["name"]}.')
    print(f'{room["description"]}')

    if not room["items"]:
        print('V miestnosti sa nenáchadzajú žiadne predmety.')
    else:
        print('V miestnosti vidis tieto predmety:')
        for item in room["items"]:
            print(f'* {item}')
        # print(f'Vidis: {", ".join(room["items"])}')

    if not room["exits"]:
        print('Z miestnosti nevedú žiadne východy.')
    else:
        print('Z miestnosti sa vies dostat von tymito vychodmi:')
        for out in room["exits"]:
            print(f'* {out}')


def show_inventory():
    if len(backpack) == 0:
        print('Tvoj batoh je prazdny')
    else:
        print('V batohu mas:')
        for item in backpack:
            print(f'* {item}')


if __name__ == '__main__':
    # init game
    room = {
        'name': 'Dungeon',
        'description': 'Nachádzaš sa v tmavej zatuchnutej miestnosti. Na kamenných stenách sa nenachádza žiadne okno, '
                       'čo dáva tušiť, \nže si niekoľko metrov pod zemou. Žeby košický hrad? Aj to je možné, '
                       'ti prebleslo hlavou.',
        'items': ['kanister', 'noviny', 'zapalky', 'hasiaci pristroj'],
        'exits': []
    }

    intro_banner()

    # main loop
    game_state = states.PLAY
    backpack = ['figa borova', 'minca']
    while game_state == states.PLAY:
        line = input('> ').lower().strip()
        if line == '':
            continue

        elif line in ('koniec', 'quit', 'q', 'bye', 'end'):
            game_state = states.QUIT

        elif line in ('o hre', 'about', 'info'):
            about_game()

        elif line in ('prikazy', 'commands', 'help', '?'):
            commands_list()

        elif line in ('rozhliadni sa', 'look around', 'show room'):
            show_room(room)

        elif line in ('inventory', 'i', 'batoh', 'backpack'):
            show_inventory()

        else:
            print('Taky prikaz nepoznam.')

    print('Thank you for playing!')
    print('(c)2021 by Darius Lindvai')
