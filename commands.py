from typing import Dict
import states
from helpers import get_item_by_name, show_room
from items import MOVABLE


def intro_banner():
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print("|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/")
    print("                       and his Great Escape                        ")
    print()


def about_game(context):
    print('Túto hru, inšpirovanú slávnym Indiana Jonesom, vytvoril začínajúci vývojár Darius Lindvai.')
    print('Na začiatku hry sa ocitnete v roli Indiana Jonesa, ktorý sa snaží uniknúť z uzamknutej miestnosti.')
    print('Vašou úlohou je preskúmať miestnosť a nájsť všetky stopy a predmety, ktoré vám pri úniku pomôžu.')


def commands_list(context):
    print('Zoznam použiteľných príkazov v hre:')
    print('* koniec/quit/q/bye/end - ukončí hru')
    print('* o hre/about/info - zobrazí základné informácie o hre')
    print('* prikazy/commands/help/?/cmd - zobrazí zoznam príkazov')
    print('* rozhliadni sa/look around/show room - zobrazí názov a opis aktuálnej miestnosti')
    print('* inventory/i/batoh/backpack - zobrazí obsah inventára')
    print('* vezmi - vezme predmet z miestnosti a vloží ho do batohu')
    print('* poloz - vyberie predmet z batohu a položí ho na zem')
    print('* preskumaj - vypíše vlastnosť daného predmetu')


def look_around(context: dict):
    show_room(context['room'])


def quit_game(context):
    context["state"] = states.QUIT


def show_inventory(context):
    if not context["backpack"]["items"]:
        print('Tvoj batoh je prázdny.')
    else:
        print('V batohu máš:')
        for item in context["backpack"]["items"]:
            print(f'* {item["name"]}')


def take_item(line, context):
    backpack = context['backpack']
    room = context['room']
    name = line.split('vezmi')[1].strip()
    if not name:
        print("Neviem, čo chceš zobrať.")
        return

    item = get_item_by_name(name, room["items"])

    if item is None:
        print('Taký predmet tu nikde nevidím.')
        return

    if MOVABLE not in item["features"]:
        print('Tento predmet sa nedá vziať.')
        return

    if len(backpack['items']) >= backpack['max']:
        print('Batoh je plný')
        return

    room["items"].remove(item)
    backpack["items"].append(item)
    print(f'Predmet {name} si si vložil do batohu.')


def drop_item(line, context):
    backpack = context['backpack']
    room = context['room']
    name = line.split('poloz')[1].strip()

    if not name:
        print("Neviem, čo chceš položiť na zem.")
        return

    item = get_item_by_name(name, backpack["items"])

    if item is None:
        print('Taký predmet sa v batohu nenachádza.')
        return

    backpack["items"].remove(item)
    room["items"].append(item)
    print(f'Predmet {name} si položil na zem.')


def inspect_item(line, context):
    name = line.split('preskumaj')[1].strip()
    if not name:
        print("Neviem, aký predmet chceš preskúmať.")
        return

    item = get_item_by_name(name, context['backpack']['items'] + context['room']['items'])

    if item is None:
        print('Taký predmet sa nikde nenachádza.')
        return

    print(item['description'])
