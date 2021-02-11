import random
import robot
import import_helper
ob = []

def use_maze(maze_ob):
    """imports the maze and uses it instead of the randomly generated obstacles"""
    global ob
    o = import_helper.dynamic_import(maze_ob)
    ob = o.get_obstacles()
    return(ob)


def get_obstacles():
    """Creates a list of tuples that represent obstacles"""
    for i in range(random.randint(1,10)):
        x = random.randint(-100,100)
        y = random.randint(-200,200)
        ob.append((x,y))
    return(ob)


def is_position_blocked(x,y):
    """checks if a certain coordinate falls within an obstacle"""
    global ob
    block = []
    for i in ob:
        val_x = i[0]
        val_y = i[1]
        if x in range(val_x,(val_x + 5)) and y in range(val_y,(val_y + 5)):
            block.append(True)
        else:
            block.append(False)

    if True in block:
        return True
    else:
        return False 


def is_path_blocked(x1,y1, x2, y2):
    """Checks if path between 2 points is obstructed by an obstacle"""
    global ob
    blocked = []
    for i in ob:
        val_x = i[0]
        val_y = i[1]
        for x in range(val_x,(val_x + 5)):
            for y in range(val_y,(val_y + 5)):           
                if x in range(x1,x2) and y == y1 or x == x1 and y in range(y1,y2) or x in range(x2,x1) and y == y1 or x == x1 and y in range(y2,y1):    
                    blocked.append(True)
                else:
                    blocked.append(False)

    if True in blocked:
        return True
    else:
        return False   


def obstacle_positions():
    """prints out the coordinates of all the obstacles present"""
    ob = get_obstacles()
    if len(ob) > 0:
        print("There are some obstacles:")
        for i in ob:
            val_x = i[0]
            val_y = i[1]
            print(f"- At position {val_x},{val_y} (to {(val_x + 4)},{(val_y + 4)})")
    else:
        pass


def ob_be_gone():
    """makes sure that obstacles are only called once when tested(resets obstacles)"""
    global ob
    ob = []
