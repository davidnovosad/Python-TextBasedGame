'''text based game for Intro to Scripting project2 by David Novosad
I call this game Escape the killer'''


def show_instructions():
    # this will show the player the instructions and commands that can be used throughout the game
    print('\nWelcome to the text based game: Escape the Killer\n')
    print(
        'The main objective of this game is to find 8 objects\nto help you defeat the feared fugitive Fletcher Jones.')
    print('\nMove commands you can use are: West, East, North, South')
    print('Additional helpful commands are: yes, no, quit')


def main():
    # all the rooms in dict. with paths to other rooms
    rooms = {

        'Attic': {'name': 'Attic', 'North': 'Upstairs Hallway'},  # players starting position
        'Upstairs Hallway': {'name': 'Upstairs Hallway', 'South': 'Attic', 'North': 'Upstairs Bedroom',
                             'East': 'Downstairs Hallway', 'item': 'bandages', },
        'Upstairs Bedroom': {'name': 'Upstairs Bedroom', 'South': 'Upstairs Hallway', 'item': 'lighter',
                             'room_extras': 'closet'},
        'Downstairs Hallway': {'name': 'Downstairs Hallway', 'West': 'Upstairs Hallway', 'North': 'Bathroom',
                               'East': 'Dining Room', 'South': 'Garage', 'item': 'gun'},
        'Bathroom': {'name': 'Bathroom', 'South': 'Downstairs Hallway', 'East': 'Bedroom', 'item': 'painkillers'},
        'Bedroom': {'name': 'Bedroom', 'West': 'Bathroom', 'South': 'Kitchen', 'item': 'Bullets',
                    'room_extras': 'wall safe'},
        'Kitchen': {'name': 'Kitchen', 'North': 'Bedroom', 'South': 'Dining Room', 'item': 'fire extinguisher'},
        'Dining Room': {'name': 'Dining Room', 'North': 'Kitchen', 'West': 'Downstairs Hallway', 'item': 'tacos',
                        'room_extras': 'book shelf'},
        'Garage': {'name': 'Garage', 'North': 'Downstairs Hallway', 'East': 'Basement', 'item': 'gasoline',
                   'room_extras': 'car'},
        'Basement': {'name': 'Basement', 'West': 'Garage', 'item': 'Fletcher Jones'}  # villain's position
    }

    # starting position defined, later this variable will change with player's input
    # termination commands for when player wants to quit the game also commands list
    directions = ['North', 'South', 'East', 'West']
    termination = ['Quit', 'quit', 'QUIT']
    commands = ['Yes', 'No']
    # the first one is definition of the starting room and the second one defines an empty inventory list
    current_room = rooms['Attic']
    inventory = []

    show_instructions()
    print('\nYou start in the Attic, good luck!')
    # actual game loop that goes forever until player does not say quit or the payer wins/ looses.
    while True:
        player_input = input('\nWhat is your move? ')  # player inputs what is their move

        print('Your Inventory\n', inventory)  # this prints inventory every time the loop repeats
        if player_input.capitalize() in directions:  # checks if input in directions list
            if player_input.capitalize() in current_room:  # checks if direction is in the current room in the dictionary
                current_room = rooms[current_room[player_input.capitalize()]]  # updates the current room
                print('You are in the {}.'.format(current_room['name']))
                if current_room['name'] == 'Basement' and len(inventory) == 8:  # defines the winning scenario
                    print('All the necessary items were collected!')
                    print('You defeated Fletcher Jones\nCongratulations, you escaped!')
                    break
                elif current_room['name'] == 'Basement' and len(inventory) != 8:  # defines the loosing scenario
                    print(
                        'You did not gather all the necessary items,\nFletcher Jones killed you!\nGood luck next time!')
                    break
                elif 'room_extras' in current_room:  # if room_extras is in current room this elif branch executes
                    print('There is a {}.'.format(current_room['room_extras']))
                    input_question = input(
                        'Would you like to check what is inside? (Yes or No) ').capitalize()  # asks for players input
                    while input_question.capitalize() != 'Yes' or input_question.capitalize() != 'No':  # loops until input is not either Yes or No
                        if input_question in commands:  # checks if input is in commands
                            if input_question.capitalize() == 'Yes':  # player wants to see that is inside
                                print('You see {}.'.format(current_room['item']))
                                add_item = input('Would you like to take the item? (Yes or No) ').capitalize()  # input to add item into the inventory
                                while add_item.capitalize() != 'Yes' or add_item.capitalize() != 'No':  # loop until add to inventory is either Yes or No
                                    if add_item.capitalize() == 'Yes':  # Yes, add to inventory, while loop breaks
                                        print('{} added to your inventory.'.format(current_room['item']))
                                        inventory.append(current_room['item'])
                                        del current_room['room_extras']  # this deletes the room_extras from dictionary so that it does not repeat if we enter the room again
                                        del current_room['item']  # this deletes the item from the inventory so that it does not show up again
                                        break
                                    elif add_item.capitalize() == 'No':  # item and stay player moves to a different room
                                        print('Continue with your exploration!')
                                        del current_room['room_extras']  # deletes the room_extras because the player already explored it before
                                        break
                                    else:
                                        add_item = input('Would you like to take the item? (Yes or No) ').capitalize()  # repeats the while loop again
                                break
                            elif input_question.capitalize() == 'No':  # player does not check what is in room_extras and continues moving between rooms
                                print('Continue on with exploration of the house.')
                                break
                        else:  # if input not in command this else branch executes and loop repeats
                            print('You must input Yes/ No! Try again!')
                            input_question = input('Would you like to check what is inside? (Yes or No) ').capitalize()
                elif 'item' not in current_room.keys():  # there is no item in the room
                    print('There is no item here, keep on looking.')
                elif current_room['item'] in current_room.values():  # item is in the room
                    print('You see {}'.format(current_room['item']))
                    add_item = input('Would you like to take the item? (Yes or No) ').capitalize() # prompt to add item to the inventory
                    while add_item.capitalize() != 'Yes' or add_item.capitalize() != 'No':  # while loop until add_item is Yes or No
                        if add_item.capitalize() == 'Yes':  # player adds the item into the inventory loop breaks
                            print('{} added to your inventory.'.format(current_room['item']))
                            inventory.append(current_room['item'])  # this line adds the item into the inventory
                            del current_room['item']  # this deletes the item from the dictionary
                            break
                        elif add_item.capitalize() == 'No':  # item stays in the room and player goes on to explore other rooms
                            print('Continue with your exploration!')
                            break
                        else:
                            add_item = input('Invalid move type Yes/ No! ').capitalize()  # repeats the while loop
            elif player_input.capitalize() not in current_room:  # if the direction player chose is not in the current room, player repeats with different direction
                print('You cannot go that way, try again!')
        elif player_input in termination:  # allows the player to quit the game
            print('Sorry to see you go. Have a nice day!')
            break
        elif player_input.capitalize() not in directions:  # if player inputs totally different word that is not in instructions
            print('Invalid move, try again!')


if __name__ == '__main__':  # runs the defined function main as the main function if there would be more documents and .py documents connected
    main()
