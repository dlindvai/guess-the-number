#!/usr/bin/env python3
import states

room = {
    'name': 'dungeon',
    'description': 'Nachádzaš sa v tmavej zatuchnutej miestnosti. Na kamenných stenách sa nenachádza žiadne okno, '
                   'čo dáva tušiť, že si niekoľko metrov pod zemou. Žeby košický hrad? Aj to je možné, ti prebleslo '
                   'hlavou.',
    'items': [],
    'exits': []
}


def show_room():
    print(f'Nachadzas sa v miestnosti {room["name"]}.')
    print(f'{room["description"]}.')


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
    print('* rozhliadni sa/look around - zobrazi nazov a opis aktualnej miestnosti')


if __name__ == '__main__':
    intro_banner()

    # main loop
    game_state = states.PLAY
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

        elif line in ('rozhliadni sa', 'look around'):
            show_room()

        else:
            print('Taky prikaz nepoznam')

    print('Thank you for playing!')
    print('(c)2021 by Darius Lindvai')
