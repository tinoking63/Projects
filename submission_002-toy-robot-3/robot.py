# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint','replay','replay reversed','replay silent','replay reversed silent']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
history = []
# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

global silent


#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.

def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command,robot_name):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command,robot_name):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    global new_list_split

    new_list_cmd = ["silent","reversed"]
    (command_name, arg1) = split_command_input(command)
    if command_name.lower() == 'replay':
        new_list = arg1.lower().split()
        new_list_split = list(filter(lambda x: x if x.isdigit() or '-' in x else '', new_list))
        if robot_range(new_list_split,robot_name) == 0:
            return False
        new_list = list(filter(lambda x: x if x.isdigit() == False and '-' not in x else '', new_list))
        # args = command.split(" ")
        for i in new_list:
            if i not in new_list_cmd:
                return False
        return True
    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1)) 
    # or args[1] == "reversed" or args[1] == 'silent' or args[1] == 'reversed silent' 


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all commands entered
REPLAY SILENT - replays all commands entered silently
REPLAY REVERSED - replays all commands entered in reverse
REPLAY REVERSED SILENT - replays all commands entered in reverse silently"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def history_command(command):
    if command != 'help' and command != 'replay' and command != 'replay reversed' and command != 'replay silent':
        history.append(command)
    return history

def handle_silent_command(robot_name, command):
    (command_name, arg) = split_command_input(command)
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command == 'replay':
        (do_next, command_output) = replay(robot_name,command)
    elif command == 'replay reversed':
        (do_next, command_output) = reverse_replay(robot_name, command)
    elif command == 'replay silent':
        (do_next, command_output) = replay_silent(robot_name, command)
    elif command == 'replay reversed silent':
        (do_next, command_output) = reverse_replay_silent(robot_name, command)

    # print(command_output)
    # show_position(robot_name)
    # history.append(command)
    # print('history', history)
    return do_next

def handle_command(robot_name, command):

    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    global new_list_split, do_next
    # silent = False

    
    command_output = ''
    # do_next = True
    (command_name, arg) = split_command_input(command)
    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command == 'replay':
        (do_next, command_output) = replay(robot_name,command,new_list_split)
    elif command == 'replay reversed':
        (do_next, command_output) = reverse_replay(robot_name, command)
    elif command == 'replay silent':
        (do_next, command_output) = replay_silent(robot_name,command)
    elif command == 'replay reversed silent':
        (do_next, command_output) = reverse_replay_silent(robot_name, command)
    
    print(command_output)
    if command_name != 'help':
        show_position(robot_name)
    return do_next

def replay(robot_name,command,new_list_split):
    for i in history:
        # if new_list_split.isdigit():
        #     robot_range(new_list_split)
        #     handle_command(robot_name,i)
        # else:
        handle_command(robot_name,i)
    return(True, f" > {robot_name} replayed {len(history)} commands.")
    # for n in history:
    #     if n == (len(history)-1)
    #         handle_command(robot_name,i)
    # return(True, f"{robot_name} replayed {len(history)} commands.")


def reverse_replay(robot_name, command):
    for i in reversed(history):
        handle_command(robot_name,i)
    return(True, f" > {robot_name} replayed {len(history)} commands in reverse.")


def replay_silent(robot_name,command):
    for i in history:
        # print(i, history)
        handle_silent_command(robot_name,i)
    return(True, f" > {robot_name} replayed {len(history)} commands silently.")

    # silent = True

    # list(map(lambda x: handle_command(robot_name,x),history))

    # silent = False
    # return (True, f"{robot_name} replayed {len(history)} command.")


def short_command(robot_name, command,n,m):
    global history


def reverse_replay_silent(robot_name, command):
    for i in reversed(history):
        handle_silent_command(robot_name,i)
    return(True, f" > {robot_name} replayed {len(history)} commands in reverse silently.")


def robot_range(new_list_split,robot_name):
    
    if len(new_list_split) > 0:
        new_list_split = new_list_split[0]
        new_list_split1 = new_list_split.split("-", 1)
        num1 = int(new_list_split1[0])
        
        if new_list_split.isdigit():
            output = [handle_command(robot_name, i) for i in history[-num1::]]
            print(f" > {robot_name} replayed {int(new_list_split)} commands.")

        elif '-' in new_list_split:
            num2 = int(new_list_split1[1])
            
            if new_list_split1[0].isdigit() and new_list_split1[1].isdigit():
                new_var = [handle_command(robot_name, i) for i in history[-num1: -num2]]
                print(f" > {robot_name} replayed {(num1 - num2)} commands.")
                return True, new_var
            
            else:
                return False
        return (len(history) - int(new_list_split1[0]), len(history))

    else:
        return (0, len(history))


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index, history

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0
    history = []

    command = get_command(robot_name)
    while handle_command(robot_name, command):
        history = history_command(command)
        command = get_command(robot_name)
    while handle_silent_command(robot_name, command):
        history = history_command(command)
        command = get_command(robot_name)
    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()


