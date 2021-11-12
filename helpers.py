from typing import List


def get_item_by_name(name: str, items: List[dict]) -> dict:
    for item in items:
        if name == item['name']:
            return item
