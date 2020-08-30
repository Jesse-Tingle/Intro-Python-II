# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from item import Item


class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f"{self.current_room} {self.items}"

    def get_inventory_item(self, item_name: str):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        else:
            return None

    def remove_inventory_item(self, item: Item):
        self.items.remove(item)
