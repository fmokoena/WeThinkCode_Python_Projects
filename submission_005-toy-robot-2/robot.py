x = 0
y = 0
direction = 0
run = True

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
    valid_ls = ["off","help","forward","back","right","left","sprint",]
    move = command.split()
    if command.casefold() in valid_ls or move[0].casefold() in valid_ls:
        if command.casefold() ==  "off":
            print(f"{name}: Shutting down..")
            run = False
        elif command.casefold() == "help":
            print("""I can understand these commands:

    OFF  - Shut down robot

    HELP - provide information about commands

    forward 0 - moves the robot forward "0" steps 
    "0" represents a value that you must input

    back 0 -  moves the robot backwards "0" steps
    "0" represents a value that you must input

    right - turns the robot right

    left - turns the robot left

    sprint - gives the robot a short burst of speed and extra distance
    """)
    else:
        print(f"{name}: Sorry, I did not understand '{command}'.")

def robot_movement(command, name):
    """makes sure the robot moves according to the users command"""
    if command.casefold() == "right":
        return turn_right(name)

    elif command.casefold() == "left":
        return turn_left(name)

    move = command.split()
    if move[0].casefold() == "forward":
        return move_forward(move, name)

    elif move[0].casefold() == "back":
        return move_back(move, name)

    elif move[0].casefold() == "sprint":
        jog = int(move[1])
        return move_sprint(move, jog, [], name)

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
    range_x = x + move_x
    range_y = y + move_y

    if range_x > 100 or range_x < -100 or range_y > 200 or range_y < -200 :
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        move_x = 0
        move_y = 0
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
    x_axis = x + move_x
    y_axis = y + move_y
    x = x_axis
    y = y_axis
    print(f" > {name} now at position ({x_axis},{y_axis}).")
    return 

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
    y = 0
    x = 0
    direction = 0
    run = True
if __name__ == "__main__":
    robot_start()