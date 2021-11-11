#!/usr/bin/env python3


if __name__ == '__main__':
    # print('Welcome to the game:')
    # print('INDIANA JONES AND THE ESCAPE FROM DARK ROOM')
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print("|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/")
    print("                       and his Great Escape                        ")
    print()

    # parameters
    line = None

    # main loop
    while True:
        line = input('> ').lower().strip()
        if line in '':
            continue

        elif line in ('koniec', 'quit', 'q', 'bye', 'end'):
            break

        elif line in ('o hre', 'about', 'info'):
            print('Túto hru, inšpirovanú slávnym Indiana Jonesom, vytvoril začínajúci vývojár Darius Lindvai.')
            print('Na začiatku hry sa ocitnete v roli Indiana Jonesa, ktorý sa snaží uniknúť z uzamknutej miestnosti.')
            print('Vašou úlohou je preskúmať miestnosť a nájsť všetky stopy a predmety, ktoré vám pri úniku pomôžu.')

        elif line in ('prikazy', 'commands', 'help', '?'):
            print('Zoznam pouzitelnych prikazov v hre:')
            print('* o hre/about/info - dozviete sa zakladne informacie o hre')
            print('* prikazy/commands/help/? - zobrazi zoznam prikazov')
            print('* koniec/quit/q/bye/end - ukonci hru')

        else:
            print('Taky prikaz nepoznam')

    print('Thank you for playing!')
    print('(c)2021 by Darius Lindvai')
