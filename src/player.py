# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def pick_up(self, item):
        self.inventory.append(item)
        self.current_room.items.remove(item)

    def drop(self, item):
        self.inventory.remove(item)

    def view_inventory(self):
        for i in self.inventory:
            print(f"{i.item_name}: {i.item_description}")

    def __str__(self):
        return f"{self.name} is in {self.current_room}"
