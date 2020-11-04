import turtle
from world import obstacles
import robot
# from world.obs





# print(obstacles.create_obs_coords)
robot = turtle.Screen()
robot.bgcolor("black")

position_x = 0
position_y = 0
current_direction_index = 0
directions = ['forward', 'right', 'back', 'left']
min_y, max_y = -200, 200
min_x, max_x = -100, 100

valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left', 'sprint']
move_commands = valid_commands[3:]

def border():
    '''
    This turle produces the border
    '''

    turt = turtle.Turtle()
    turt.penup()
    turt.setposition(-200,-200)
    turt.pendown()
    turt.pensize(10)
    turt.pencolor('green')
    turt.speed(-1)
    for i in range(4):
        turt.forward(400)
        turt.left(90)
    turt.hideturtle()


def create_player():
    '''
    This produces the turtle/player that you control
    '''
    global player
    player = turtle.Turtle()
    player.left(90)
    player.color('green')
    player.shape("classic")
    player.penup()



def create_obs():
    '''
    This displays the obstacles on the turtle screen 
    '''
    my_obs_turt = turtle.Turtle()
    my_obs_turt.hideturtle()
    my_obs_turt.color('red')
    list_of_coords = obstacles.get_obstacles()
    my_obs_turt.speed(20)
    my_obs_turt.penup()
    for i in range(len(list_of_coords)):
        my_obs_turt.setposition(list_of_coords[i])
        my_obs_turt.begin_fill()
        for j in range(4):
            my_obs_turt.pendown()
            my_obs_turt.forward(5)
            my_obs_turt.right(90)
        my_obs_turt.end_fill()
        my_obs_turt.penup()
        

def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """
    
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 1 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()

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
    
    obstacles.obs_true = False
    if obstacles.is_position_blocked(new_x, new_y) or obstacles.is_path_blocked(new_x, new_y,position_x,position_y):
        return "blocked"
    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False

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

def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    global player
    if  update_position(steps) == True:
        player.forward(steps)

        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif update_position(steps) == 'blocked':
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    global player
    if update_position(-steps) == True:
        player.back(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'

    elif update_position(-steps) == 'blocked':
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'

    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index,player
    
    current_direction_index += 1
    player.right(90)
    if current_direction_index > 3:
        current_direction_index = 0
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index,player

    current_direction_index -= 1
    player.left(90)
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



create_player()
border()
create_obs()
