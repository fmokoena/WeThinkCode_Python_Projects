import world.obstacles as obstacles
x = 0
y = 0
   

def check_position_range(move_y, move_x, move, name, silent):
    """makes sure the robot is within the set range and that it doesnt move over obstacles """
    global x
    global y

    range_x = x + move_x
    range_y = y + move_y
    block = obstacles.is_position_blocked(range_x,range_y)
    blocked = obstacles.is_path_blocked(x,y ,range_x,range_y)

    if range_x > 100 or range_x < -100 or range_y > 200 or range_y < -200 :
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        move_x = 0
        move_y = 0
        return track_position(move_y, move_x, name, silent)

    elif block == True or blocked == True:
        print("Sorry, there is an obstacle in the way.")
        move_x = 0
        move_y = 0
        return track_position(move_y, move_x, name, silent)
    
    elif silent == True:
        return track_position(move_y, move_x, name, silent)

    elif move[0] == "sprint":
        num = int(move[1])
        while num > 0:
            print(f" > {name} moved forward by {num} steps.")
            num-= 1
        return track_position(move_y, move_x, name, silent)

    else:
        print(f" > {name} moved {move[0].lower()} by {move[1]} steps.")
        return track_position(move_y, move_x, name, silent)

def track_position(move_y, move_x, name, silent):
    """keeps track of the robots postion"""
    global x
    global y

    x_axis = x + move_x
    y_axis = y + move_y
    x = x_axis
    y = y_axis
    if silent == False:
        print(f" > {name} now at position ({x_axis},{y_axis}).")


#ef obstacle_positions():
#   """prints out the coordinates of all the obstacles present"""
#   ob = obstacles.get_obstacles()
#    print("There are some obstacles:")
#    for i in ob:
#        val_x = i[0]
#        val_y = i[1]
#        print(f"- At position {val_x},{val_y} (to {(val_x + 4)},{(val_y + 4)})")


def blobal_bariables(blx):
    """resets the global variables"""
    global x
    global y

    x = blx
    y = blx
