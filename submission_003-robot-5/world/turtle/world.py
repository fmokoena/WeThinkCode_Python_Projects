import turtle
import maze.obstacles as obstacles

x = 0
y = 0

def set_turtle_enviroment():
    """Sets up the turtle enviroment"""
    windo=turtle.Screen()
    windo.bgcolor("honeydew")
    windo.setworldcoordinates(-200, -200, 200, 200)
    #Draw Border
    border = turtle.Turtle()
    border.speed(50)
    border.penup()
    border.setposition(-100,-200)
    border.pendown()
    border.forward(200)
    border.left(90)
    border.forward(400)
    border.left(90)
    border.forward(200)
    border.left(90)
    border.forward(400)
    border.hideturtle()

    global bmo
    bmo = turtle.Turtle()
    bmo.color("teal")
    bmo.penup()
    bmo.left(90)


def robot_turn(turn):
    """turns the turtle"""
    global bmo
    if turn == "right":
        bmo.right(90)
    else:
        bmo.left(90)


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

    elif move[0] == "sprint":
        return track_position(move_y, move_x, name, silent)

    else:    
        return track_position(move_y, move_x, name, silent)


def track_position(move_y, move_x, name, silent):
    """keeps track of the robots postion and moves the robot """
    global bmo
    global x
    global y
    x_axis = x + move_x
    y_axis = y + move_y
    x = x_axis
    y = y_axis
    turtle.tracer(n = 1)
    bmo.goto(x_axis,y_axis)
    print(f" > {name} now at position ({x_axis},{y_axis}).")


def create_obstacles():
    """Creates the obstacles in the turtle enviroment"""
    ob = obstacles.ob
    turtle.tracer(n = 0)
    orb = turtle.Turtle()
    orb.speed(0)
    for i in ob:
        val_x = i[0]
        val_y = i[1]
        orb.penup()
        orb.setposition(val_x ,val_y )
        orb.pendown()
        orb.begin_fill()
        for r in range(4):
            orb.color("olive")
            orb.forward(5)
            orb.left(90)
        orb.end_fill()
    orb.hideturtle()


def reset_postion():
    """resets the postion and of the turtle to the start point(postion 0,0)"""
    global bmo
    global x
    global y
    x = 0
    y = 0
    bmo.goto(0,0)
    bmo.setheading(90)
    print(f" bot is facing {str(bmo.heading())}")


def blobal_bariables(blx):
    """resets the global Variables"""
    global x
    global y

    x = blx
    y = blx