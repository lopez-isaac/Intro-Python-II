from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

#create items
sword = Item("sword", "Rusty but still cuts")
shield =Item("shield", "Made from fine oak wood")
helmet = Item("helmet", "Keeps your hair dust free, unless your bald")
apple = Item("apple", "Juicy and sweet")
gold = Item("gold", "1000 gold coins")
telescope = Item("telescope", "A golden telescope")


#add items to rooms
room["foyer"].items.append(sword)
room["foyer"].items.append(shield)
room["foyer"].items.append(helmet)
room["outside"].items.append(apple)
room["treasure"].items.append(gold)
room["overlook"].items.append(telescope)

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Isaac", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
#

usr_input = " "
print("Find the treasure room!!")
print("""How to play:
Movements:[n] [s] [e] [w] [q]uit
Actions: [get item] [drop item] [i]nventory""")

while usr_input != "q":
    print("---------------------")
    print(player1)
    player1.current_room.list_items()
    usr_input = str(input("Enter command:"))

    if usr_input == "get item":
        player1.current_room.list_items()
        item_input = input("select item to pick up:")
        #item=None
        for i in player1.current_room.items:
            if i.item_name == item_input:
                item = i
            else:
                print("invalid")
        player1.pick_up(item)
        item.on_take()

    elif usr_input == "drop":
        print("inventory contains:")
        player1.view_inventory()
        item_input = input("select item to drop up:")
        # item=None
        for i in player1.inventory:
            if i.item_name == item_input:
                item = i
            else:
                print("invalid")
        player1.drop(item)
        item.on_drop()

    elif usr_input == "i":
        print("inventory contains:")
        player1.view_inventory()

    elif usr_input == "n":
        if player1.current_room.n_to == None:
            print("\nDead end try again\n")
        else:
            player1.current_room = player1.current_room.n_to

    elif usr_input =="s":
        if player1.current_room.s_to == None:
            print("Dead end try again\n")
        else:
            player1.current_room = player1.current_room.s_to

    elif usr_input =="e":
        if player1.current_room.e_to == None:
            print("Dead end try again\n")
        else:
            player1.current_room = player1.current_room.e_to

    elif usr_input =="w":
        if player1.current_room.w_to == None:
            print("Dead end try again\n")
        else:
            player1.current_room = player1.current_room.w_to











