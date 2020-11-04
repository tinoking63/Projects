
import random
import turtle
list_co = []

my_obs_turt = turtle.Turtle()
    # my_obs_turt.hideturtle()
my_obs_turt.color('orange')
my_obs_turt.shape("square")
    # list_of_coords = get_obstacles()
my_obs_turt.speed(0)
    # print(list_of_coords)
my_obs_turt.penup()


my_maze = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]



def maze(my_maze):
    '''
    This displays the obstacles on the turtle screen 
    '''
    for y in range(len(my_maze)):
        for x in range(len(my_maze[y])):
            chara = my_maze[y][x]

            scrn_x = -190 +(x * 10)
            scrn_y = -190 + (y * 20)

            if chara == 'X':
                obs0 = (scrn_x,scrn_y)
                list_co.append(obs0)

# def is_position_blocked(x, y):
#     '''
#     This checks if the positon of the obstacle is blocked
#     '''
#     global list_co, obs_true
    
#     for i in list_co:
#         if x == i[0] and y == i[1] or (x <= i[0] + 4 and x >= i[0]) and (y <= i[1] + 4 and y >= i[1]) or x ==i[0] + 4 and y == i[1] + 4:
#             obs_true = True
#             return True
#     obs_true = False
#     return obs_true


# def is_path_blocked(x1, y1, x2, y2):
#     '''
#     This checks if the path of the obstacle is blocked.
#     The player(turtle) can't go pass it
#     '''
#     global list_co, obs_true
    
#     for i in list_co:
#         if x1 == x2:
#             if (y1 <= i[1] <= y2 or y1 >= i[1] >= y2) and i[0] <= x1 <= i[0] + 4:
                
#                 obs_true = True
#                 return True

#         if (x1 <= i[0] <= x2 or x1 >= i[0] >= x2) and i[1] <= y1 <= i[1] + 4:               
#                 obs_true = True
#                 return True
#     obs_true = False
#     return obs_true

# def get_obstacles():
#     '''
#     This produces and random integer and also generates the obstacles
#     '''
#     global list_co
#     x = 0
#     y = 0
#     for i in range(1, random.randint(1, 11)):
#         x = random.randint(-99, 99)
#         y = random.randint(-199, 199)
#         tup = (x, y)
#         list_co.append(tup)
#         # print(list_co,"list_co")
#     return list_co

# maze(my_maze)