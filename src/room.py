# Implement a class to hold room information. This should have name and
# description attributes.

class Room():

    def __init__(self, name, description,):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def list_items(self):
        if self.items == []:
            print("There aren't any items around.")
        else:
            print("This area contains:")
            for item in self.items:
                print(f"{item.item_name}: {item.item_description}")





    def __str__(self):
        return f"{self.name} {self.description}"
