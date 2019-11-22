from room import Room
from player import Player
from item import Gold
from item import Food

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Food('banana', 'is a bit bruised', 20), Gold(100)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Too bad grasshopper, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Gold(1000000)])
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

def tryDirection(d, curr_room):
    # Try to move a direction or print an error if the player cant go that way. Returns the room the player has moved to (or the same room if the player didnt move)

    attrib = d + '_to'


    if hasattr(curr_room, attrib):

        return getattr(curr_room, attrib) 

    print("You cant go that way")

    return curr_room

# Make a new player object that is currently in the 'outside' room.
player = Player("Jordan", room["outside"])
print(f'Welcome to the Matrix of Python {player.name}!')

done = False    

while not done:

# print the room name
    print("You are currently located at: \n{}\n".format(player.curr_room.name))

# print the room description
    print(player.curr_room.description)

# print the room items
    for item in player.curr_room.items:
        print(item)

#user prompt
    s = input("\nCommand>").strip().lower().split()

# User prompt
    if len(s) !=1:
        print("I dont understand that")
        continue

     # Intransitive Verbs

    if s[0] == "quit" or s[0] == "q":
        print(f'Thanks for playing {player.name}!')
        done = True

    elif s[0] in ["n", "s", "w", "e"]:
        player.curr_room = tryDirection(s[0], player.curr_room)

    else:
        print('Unknown command {}'.format(''.join(s)))

    
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

#print the room items
# for item in player.curr_room.items:
    # print(item)
#     print(item.inspect()) - put in a str in room class



##################### Possible another direction #####################
# while True:
#     print(f"\n Hey {new_player.name}! Your current location is {new_player.curr_room}")
#     print("=======================")

#     direction = input("Enter a direction: ") #this will be the command in the method get_direction
#     if direction == "q":
#         print("Thanks for playing grasshopper! Bye!")
#         break
#     if direction == "n" or direction == "s" or direction == "e" or direction == "w":
#         new_room = new_player.curr_room.retrieve_direction(direction)
#         #player_1.change_location(new_room)
#         if new_room == None:
#             print("Whoops! You cannot move in that direction. Try again.")
#             print("===========")
#         else:
#             new_player.change_location(new_room)