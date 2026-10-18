"""Project Two starter for the student's text-based adventure game."""

# Shantelle Lowery


def show_instructions():
    """Display the game objective and available commands."""
    # Game title and storyline.
    print("Welcome to Echoes of the Asylum. Enter...if you dare.")
    print("You wake up on the floor of an old, abandoned asylum...")
    print("There's a rumor that the old warden still lingers here. Waiting to catch anyone trying to escape.")
    print("You must find the key items and escape before Warden Graves finds you.")

    # Available commands.
    print("\nMove commands: go north, go south, go east, go west")
    print("To collect items: get 'item name'")
    print("Escape command: use Exit Key")
    print("----------------------------------------")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    # Shows the current room.
    print(f"\nYou are in the {current_room}.")

    # Shows current inventory.
    print(f"Inventory: {inventory}")
    
    # Shows what the current room item is - when available.
    if 'item' in rooms[current_room]:
        print(f"You see an item: {rooms[current_room]['item']}.")

    print("----------------------------------------")


def main():
    """Run the main gameplay loop."""
    # Dictionary linking the rooms, items and directions player can move.
    rooms = {
        'Reception': {
            'west': 'Patient Room',
            'north': "Warden's Office"
        },
        'Patient Room': {
            'east': 'Reception',
            'north': "Nurses' Station",
            'item': 'Old Key'
        },
        "Nurses' Station": {
            'south': 'Patient Room',
            'north': 'Treatment Room',
            'item': 'Security Badge'
        },
        'Treatment Room': {
            'south': "Nurses' Station",
            'east': 'Cafeteria',
            'item': 'Patient Diary'
        },
        'Cafeteria': {
            'west': 'Treatment Room',
            'east': 'Basement',
            'south': "Warden's Office",
            'item': 'Flashlight'
        },
        'Basement': {
            'west': 'Cafeteria',
            'south': 'Security Office',
            'item': 'Crowbar'
        },
        'Security Office': {
            'north': 'Basement',
            'west': "Warden's Office",
            'item': 'Exit Key'
        },
        "Warden's Office": {
            'north': 'Cafeteria',
            'south': 'Reception',
            'east': 'Security Office',
            'villain': 'Warden Graves'
        }
    }
        

    # Player's starting room.
    current_room = "Reception"

    # Create the player's inventory.
    inventory = []

    # Keeps track of rooms player already visited.
    visited_rooms = []

    # Call the instruction function at the start of the game.
    show_instructions()

    
    # Gameplay loop.
    game_over = False

    while game_over == False:
        # Show the player's current status.
        show_status(current_room, inventory, rooms)

        # Prompt player for their next command.
        print("Enter a command: go north/go south/go east/go west, get item name, or use Exit Key.")
        command = input("Enter your move: ").lower().strip()

        # Handle movement commands.
        if command.startswith("go "):
            move_valid = False
            movement_command = command[3:]

            # Check if the direction is valid for the current room.
            if movement_command in rooms[current_room]:
                next_room = rooms[current_room][movement_command]

                # Check if the player has the Old Key.
                if current_room == "Patient Room" and next_room == "Nurses' Station":
                    if "Old Key" in inventory:
                        print("You use the Old Key to unlock the Nurses' Station.")
                        move_valid = True
                    else:
                        print("The door is locked! You need the Old Key.")

                # Check if the player has the Security Badge.
                elif current_room == "Basement" and next_room == "Security Office":
                    if "Security Badge" in inventory:
                        print("You swipe the Security Badge against the scanner.")
                        print("A green light flashes, and the door unlocks.")
                        move_valid = True
                    else:
                        print("The room seems locked! You need the Security Badge.")

                # Check if the player has the Flashlight.
                elif current_room == "Cafeteria" and next_room == "Basement":
                    if "Flashlight" in inventory:
                        print("You turn on the Flashlight.")
                        print("The beam reveals a dark staircase leading into the Basement.")
                        move_valid = True
                    else:
                        print("It's too dark in here.. Maybe a Flashlight would help.")

                # Allow movement through other connected rooms.
                else:
                    move_valid = True

                # Update the room when movement is valid.
                if move_valid == True:
                    current_room = next_room
                    print("You moved to " + current_room)

                    # Creepy message when trying to escape with all 6 items.
                    if current_room == "Cafeteria" and len(inventory) == 6:
                        print("\nSuddenly, the sound of keys jingling echoes behind you. Closer.")
                        print("Heavy footsteps become louder.")
                        print("A low voice whispers, 'You can't leave...'")
                        print("You can feel Warden Graves is close. You need to hurry!")

                    # Creepy messages when a player enters a room for the first time.
                    if current_room not in visited_rooms:
                        if current_room == "Nurses' Station":
                            print("\nYou hear heavy slow footsteps from somewhere down the hall...")
                            print("You freeze, listening as the footsteps slowly fade away.")

                        elif current_room == "Cafeteria":
                            print("\nKeys jingle somewhere in the distance.")
                            print("You hear a door creak, followed by the click of a lock.")
                            print("Was someone unlocking a door...or locking it?")
                            print("You can't tell...")

                        # Adding the room to the visited list.
                        visited_rooms.append(current_room)

                    # Reminds player how to escape.
                    if current_room == "Reception" and len(inventory) == 6:
                        print("\nYou stand before the asylum's locked entrance.")
                        print("You have everything you need to escape!")
                        print("Type 'use Exit Key' to unlock the doors.")

            else:
                print("You cannot move in that direction.")

            # Check if the player encounters Warden Graves.
            if current_room == "Warden's Office":
                print("You hear heavy footsteps behind you...")
                print("Warden Graves has caught you!")
                print("GAME OVER")
                print("Thanks for playing Echoes of the Asylum!")
                game_over = True

        # Handle commands to collect items.
        elif command.startswith("get "):
            item_name = command[4:]

            # Check if the item is already in the inventory.
            if item_name in [item.lower() for item in inventory]:
                print("You already have that item in your inventory.")

            # Check if the item is available in the current room.
            elif "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if item_name == room_item.lower():
                    inventory.append(room_item)
                    del rooms[current_room]["item"]
                    print("You picked up the " + room_item + ".")

                    # Display the creepy Patient Diary entry.
                    if room_item == "Patient Diary":
                        print("\nYou open the worn pages of the diary...")
                        print("The last entry reads:")
                        print("'October 13th. The Warden is still here.'")
                        print("'I hear his keys dragging across the floor at night.'")
                        print("'If anyone finds this, stay away from his office.'")
                        print("'He doesn't let anyone leave...'")

                    # Display the Crowbar description.
                    elif room_item == "Crowbar":
                        print("You notice strange scratches along the Crowbar.")
                        print("Something dark stains the metal...")
                        print("You decide it's better not to ask questions.")

                    # Notify the player when all items are collected.
                    if len(inventory) == 6:
                        print("\nYou have collected all the items!")
                        print("Hurry back to Reception and use the Exit Key to escape!")

                else:
                    print("There is no " + item_name + " in this room.")

            else:
                print("There is no " + item_name + " in this room.")

        # Handle the final escape command.
        elif command == "use exit key":
            if current_room == "Reception" and len(inventory) == 6 and "Exit Key" in inventory:
                print("\nYou slide the Exit Key into the rusted lock...")
                print("The heavy doors slowly creak open.")
                print("You rush outside into the cold night air.")
                print("YOU WIN!")
                print("You have escaped Echoes of the Asylum!")
                print("Thanks for playing!")
                game_over = True
            else:
                print("You cannot escape yet!")
                print("Collect all the items and return to Reception.")

        # Handle invalid commands.
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
