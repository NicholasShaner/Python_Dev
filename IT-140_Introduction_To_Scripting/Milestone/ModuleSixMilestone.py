# Nicholas Shaner IT-140

# rooms dictionary imported from rubric
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}


# player stat funtion
def player_stat():
    print(f'{user_name}, you are in the {current_room}.')  # simple 'this is where you are'


# move function
def get_move():
    global current_room, move, player_stat  # imports global variables to allow modification within function
    # user input for a direction to move
    get_move = input('Enter a direction to go (North/South/East/West) or Exit to leave: ').capitalize().strip()
    if get_move not in ('North', 'South', 'East', 'West', 'Exit'):  # input validation
        print('Sorry, that\'s not an option.')
        get_move = input('Enter a direction to go (North/South/East/West) or Exit to leave: ').capitalize().strip()
    else:  # if move input is valid
        move = get_move
        return move


user_name = input('Enter name: ').capitalize()  # personalization
print(f'Hello {user_name}!')
move = ''  # blank string for function and validation
current_room = 'Great Hall'  # current room string


# gameplay function
def play():
    global current_room, get_move, player_stat  # imports global variable to allow modification and validation

    while True:  # endless loop until exit
        player_stat()  # function call to display player_stat
        get_move()  # function call to get_move

        if move == 'Exit':  # termination statement allowing for game exit
            current_room = 'Exit'  # resets current room to exit
            print('Current room:', current_room + ' room.')
            print('Thanks for playing {}!'.format(user_name))
            break  # breaks program to exit

        if move != 'Exit':  # loop body statement for continuing gameplay
            if move in rooms[current_room].keys():  # if move request is valid to rooms dictionary
                current_room = rooms[current_room][move]  # rewrites current room value
                continue  # restarts while loop
            elif move not in rooms[current_room].keys():  # validation loop for invalid or move request
                print('Sorry, Cant go that way.')


play()  # function call to initiate gameplay
