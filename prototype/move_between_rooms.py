"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# set starting room for player
current_room = 'Great Hall'

# gameloop will continue until player exits
while current_room != 'exit':
    print(f'\nYou are in the {current_room}.')
    
# Ask player to enter a direction
    command = input('Enter a direction (go north, go south, go east, go west, or exit): ').lower().strip()
    
# See if player wants to exit
    if command == 'exit':
        current_room = 'exit'

# Make sure valid direction is entered    
    elif command in ['go north', 'go south', 'go east', 'go west']:
        direction = command.split()[1]
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            print(f'You moved to the {current_room}.')
            
# This will handle invalid directions
        else:
            print('Whoops! You cannot go that way.')
    else:
        print('Invalid direction. Try a different way.')
        
# Message that displays when player leaves
print('Thanks so much for playing! Come back soon!')
