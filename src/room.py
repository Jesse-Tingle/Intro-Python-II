# Implement a class to hold room information. This should have name and
# description attributes.
from typing import List
from item import Item


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None
        self.items: List[Item] = []

    def __str__(self):
        return f"{self.name}: {self.description}"

    def get_item(self, item_name: str):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        else:
            return None

    def remove_item(self, item: Item):
        self.items.remove(item)
