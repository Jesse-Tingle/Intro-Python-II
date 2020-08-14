from room import Rooms
from player import Player

# Declare all the rooms

rooms = {
    'outside':  Rooms("Outside Cave Entrance",
                      "North of you, the cave mount beckons"),

    'foyer':    Rooms("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Rooms("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Rooms("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Rooms("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']


rooms['outside'].items.append

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(rooms['outside'])

# Write a loop that:
while True:
    current_room = player.current_room
    print(f"You are now in the {player.current_room.name}")
    print(player.current_room.description)

    user_input = input("Choose a direction to move in 'n', 's', 'e', 'w': \n")

    if user_input == 'n':
        if current_room.n_to:
            player.current_room = current_room.n_to
        else:
            print('Please choose a different direction!')
            continue
    if user_input == 's':
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
        else:
            print('Please choose a different direction!')
            continue
    if user_input == 'e':
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
        else:
            print('Please choose a different direction!')
            continue
    if user_input == 'w':
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
        else:
            print('Please choose a different direction!')
            continue
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
