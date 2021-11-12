from typing import List, Dict


def get_item_by_name(name: str, items: List[dict]) -> dict:
    for item in items:
        if name == item['name']:
            return item


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
