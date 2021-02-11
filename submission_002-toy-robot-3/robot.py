import re
x = 0
y = 0
direction = 0
run = True
h_st = []
silent = False

def name_robot():
    """allows the user to name the robot by taking in input from the user """
    name = input("What do you want to name your robot? ")
    print(f"{name}: Hello kiddo!")
    return name

def given_command(name):
    """allows the user to tell the robot how to move by taking in input from the user"""
    command = input(f"{name}: What must I do next? ")
    return command

def process_command(command, name):
    """takes in the users commands, makes sense of them and prints or runs the appropriate function"""
    global run
    valid_ls = ["off","help","forward","back","right","left","sprint","replay"]
    move = command.split()
    if move[0].casefold() in valid_ls:
        command_history(command)
        silence_(command)
        if command.casefold() ==  "off":
            print(f"{name}: Shutting down..")
            run = False
        elif command.casefold() == "help":
            print("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - moves the robot forward  
BACK -  moves the robot bacK
RIGHT - turns the robot right
LEFT - turns the robot left
SPRINT - gives the robot a short burst of speed and extra distance
REPLAY - replays previous movements
SILENT - only prints position when robot is replayed
REVERSE - replays previous movements in backwards order
    """)
    else:
        print(f"{name}: Sorry, I did not understand '{command}'.")

def command_history(command):
    global h_st
    valid_l_st = ["forward","back","right","left","sprint"]
    move = command.split()
    if command.casefold() in valid_l_st or move[0].casefold() in valid_l_st:
        h_st.append(command)
    return h_st

def robot_movement(command, name):
    """makes sure the robot moves according to the users command"""
    move = re.split("-| ",command.lower())
    replay_ls = ["replay","silent","reversed"]

    if command.casefold() == "right":
        return turn_right(name)

    elif command.casefold() == "left":
        return turn_left(name)

    if move[0].casefold() == "forward":
        return move_forward(move, name)

    elif move[0].casefold() == "back":
        return move_back(move, name)

    elif move[0].casefold() == "sprint":
        jog = int(move[1])
        return move_sprint(move, jog, [], name)

    elif move[0].casefold() == "replay":
        move.sort()
        if command.casefold() ==  "replay":
            mm = []
            return replay_range(command, name, mm)

        elif move[0].casefold() not in replay_ls:
            try:
                mm = filter(lambda x:False if x in replay_ls else True ,move)
                mm = list(mm)
                for i in mm:
                    int(i)
                return replay_range(command, name, mm)
            except ValueError:
                print(f"{name}: Sorry, I did not understand '{command}'.")

        elif "silent" in move or "reversed" in move:
            mm = []
            return replay_range(command, name, mm)

        else:
            print(f"{name}: Sorry, I did not understand '{command}'.")
           

def replay_range(command, name, mm):
    global h_st
    n_m = mm
    le_n = len(n_m)

    if le_n == 1:
        nb = len(h_st)
        r = int(n_m[0]) - 1
        for i in range((r+1),nb):
            p = i
        replay_movement(command, name, nb, r, p,le_n)

    elif le_n == 2:
        nb = int(n_m[1]) - 1
        r = int(n_m[0]) - 1
        p = 0
        for i in range((r+1),(nb+1)):
            p = p+1
        replay_movement(command, name, nb, r, p, le_n)

    else:
        nb = len(h_st)
        r = 0
        p = nb
        replay_movement(command, name, nb, r, p,le_n)
    

def replay_movement(command, name, nb, r, p,le_n):
    move = command.split()
    if "reversed" in  move or "REVERSED" in move:
        if le_n == 1:
            nb = nb - r
            r = 0
            replay_reversed(command,name, nb, r, p) 
        else:
            replay_reversed(command,name, nb, r, p) 
    else:
        replay_forward(command, name, nb, r, p)

def replay_forward(command, name, nb, r, p): 
    global silent 
    while r < nb:
        command = h_st[r]
        robot_movement(command,name)
        return replay_forward(command, name, nb, (r+1), p)
 
    if silent == False:
        print (f" > {name} replayed {p} commands.")
        return track_position(0, 0, name)
    else:
        print (f" > {name} replayed {p} commands silently.")
        silent = False
        return track_position(0, 0, name)

def replay_reversed(command, name, nb, r, p): 
    global silent
    while r < nb:
        command = h_st[nb-1]
        robot_movement(command,name)
        return replay_reversed(command, name, (nb-1) ,r ,p)

    if silent == False:
        print (f" > {name} replayed {p} commands in reverse.")
        return track_position(0, 0, name)
    else:
        print (f" > {name} replayed {p} commands in reverse silently.")
        silent = False
        return track_position(0, 0, name)

def silence_(command):
    global silent
    move = command.split()
    if "silent" in move or "SILENT" in move:
        silent = True
    else:
        silent = False
    return silent

def turn_right(name):
    """turns the robot right"""
    global direction
    if direction < 3:
        direction = direction + 1
    else:
        direction = 0
    move_y = 0 
    move_x = 0
    print (f" > {name} turned right.")
    return track_position(move_y, move_x, name)

def turn_left(name):
    """turns the robot left"""
    global direction
    if direction > -3:
        direction = direction - 1
    else:
        direction = 0
    move_y = 0 
    move_x = 0
    print (f" > {name} turned left.")
    return track_position(move_y, move_x, name)

def move_forward(move, name):
    """moves the robot forward """
    steps = int(move[1])
    if direction == 0:
        move_y = steps
        move_x = 0
    elif direction == 1 or direction == -3:
        move_x = steps 
        move_y = 0
    elif direction == -1 or direction == 3:
        move_x = (-steps) 
        move_y = 0
    elif direction == 2 or direction == -2:
        move_y = (-steps) 
        move_x = 0

    return check_position_range(move_y, move_x, move, name)

def move_back(move, name):
    """moves the robot backwards"""
    steps = int(move[1])
    if direction == 0:
        move_y = (-steps)
        move_x = 0
    elif direction == 1 or direction == -3:
        move_x = (-steps) 
        move_y = 0
    elif direction == -1 or direction == 3:
        move_x = (steps) 
        move_y = 0
    elif direction == 2 or direction == -2:
        move_y = (steps) 
        move_x = 0

    return check_position_range(move_y, move_x, move, name)

def move_sprint(move, jog, sprint,name):
    """gives the robot a short burst of speed and moves extra distance forward"""

    if jog > 0 :
        sprint.append(jog)
        jog -= 1
        move_sprint(move, jog, sprint, name)
    else:
        sprint = sum(sprint)
        if direction == 0:
            move_y = sprint
            move_x = 0
        elif direction == 1 or direction == -3:
            move_x = sprint 
            move_y = 0
        elif direction == -1 or direction == 3:
            move_x = (-sprint) 
            move_y = 0
        elif direction == 2 or direction == -2:
            move_y = (-sprint) 
            move_x = 0

        return check_position_range(move_y, move_x, move, name)


def check_position_range(move_y, move_x, move, name):
    """makes sure the robot is within the set range """
    global x
    global y
    global silent
    range_x = x + move_x
    range_y = y + move_y

    if range_x > 100 or range_x < -100 or range_y > 200 or range_y < -200 :
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        move_x = 0
        move_y = 0
        return track_position(move_y, move_x, name)
    
    elif silent == True:
        return track_position(move_y, move_x, name)

    elif move[0] == "sprint":
        num = int(move[1])
        while num > 0:
            print(f" > {name} moved forward by {num} steps.")
            num-= 1
        return track_position(move_y, move_x, name)

    else:
        print(f" > {name} moved {move[0].lower()} by {move[1]} steps.")
        return track_position(move_y, move_x, name)

def track_position(move_y, move_x, name):
    """keeps track of the robots postion"""
    global y
    global x
    global silent
    x_axis = x + move_x
    y_axis = y + move_y
    x = x_axis
    y = y_axis
    if silent == False:
        print(f" > {name} now at position ({x_axis},{y_axis}).")


def robot_start():
    """This is the entry function, do not change"""
    global run
    name = name_robot()
    while run == True:
        command = given_command(name)
        process_command(command, name)
        robot_movement(command, name)
    global y
    global x
    global direction 
    global h_st 
    global silent
    h_st = []
    y = 0
    x = 0
    direction = 0
    run = True
    silent = False
if __name__ == "__main__":
    robot_start()