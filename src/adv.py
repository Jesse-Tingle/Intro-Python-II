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

# Items
room['outside'].items.append(
    Item("Sword", "A bladed melee weapon. Use this to kill enemies on your quest!"))
room['narrow'].items.append(Item(
    'Shield', 'A piece of personal armour held in the hand. Use it to protect yourself against attacts from the enemy!'))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
while True:
    current_room = player.current_room
    # print(player.items)
    inventory = player.items
    # if len(inventory) > 0:
    #     print("Inventory: ")
    #     for i in range(len(inventory)):
    #         print(inventory[i])

    print(f"You are now in the {player.current_room.name}")
    print(player.current_room.description)
    # print(f"Inventory: {inventory}")

    # Print items in the player's current_room
    if len(current_room.items) == 0:
        print('This room is empty!')
    else:
        print("This room contains:")
        for item in current_room.items:
            print(item)

    # User chooses a direction or picks up/drops item
    user_input = input(
        "Choose a direction to move in 'n', 's', 'e', 'w'.\nUse 'get item' or 'drop item' to pick up or drop an item you have found in a room. \n")

    # User quits game
    if user_input == 'q':
        break

    split_input = user_input.split()
    if len(split_input) == 1:  # move the player or get inventory
        if user_input == 'i':
            if len(inventory) > 0:
                print("Inventory: ")
                for i in range(len(inventory)):
                    print(inventory[i])
            elif len(inventory) == 0:
                print("You have no items in your inventory!")

        # User goes north
        if user_input == 'n':
            if current_room.n_to:
                player.current_room = current_room.n_to
            else:
                # if user types an invalid input it will ask the user to try again
                print('Please choose a different direction!')
                continue
        # User goes south
        if user_input == 's':
            if current_room.s_to is not None:
                player.current_room = current_room.s_to
            else:
                # if user types an invalid input it will ask the user to try again
                print('Please choose a different direction!')
                continue
        # User goes east
        if user_input == 'e':
            if current_room.e_to is not None:
                player.current_room = current_room.e_to
            else:
                # if user types an invalid input it will ask the user to try again
                print('Please choose a different direction!')
                continue
        # User goes west
        if user_input == 'w':
            if current_room.w_to is not None:
                player.current_room = current_room.w_to
            else:
                # if user types an invalid input it will ask the user to try again
                print('Please choose a different direction!')
                continue
    elif len(split_input) == 2:
        # Get/Drop
        if split_input[0].lower() == 'get':
            item_name = split_input[1]
            item = current_room.get_item(item_name)
            if item:
                item.on_take()
                # remove the item from the room
                current_room.remove_item(item)
                # Add it to the player's Items
                player.items.append(item)
            else:
                print(f"{item_name} does not exist here!")
        elif split_input[0] == 'drop':
            print('drop item')

#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
