import numpy
import robot
import maze.obstacles as obstacles
import world

def mazerunner(name, command, enviroment):
    """is responsible for determining the direction of the mazerun"""
    start = 40,20
    print(f"> {name} starting maze run..")

    if "turtle" in enviroment:
        robot.env = True
        
    
    move = command.split()
    if len(move) > 1:
        if move[1] == "top":
            the_matrix(name,start,"top")
        if move[1] == "bottom":
            the_matrix(name,start,"bottom")
        if move[1] == "left":
            the_matrix(name,start,"left")
        if move[1] == "right":
            the_matrix(name,start,"right")
    else:
        the_matrix(name,start,"top")


def maze_direction(direction,matrix):
    """determines the end postion for the back track"""
    d_r_c_i_n = []
    if direction == "bottom":
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                d_r_c_i_n.append(i)
        r = int(len(d_r_c_i_n)/2)
        end = 0,d_r_c_i_n[r]
        return end

    if direction == "top":
        for i in range(len(matrix[-1])):
            if matrix[-1][i] == 0:
                d_r_c_i_n.append(i)
        r = int(len(d_r_c_i_n)/2)
        end = 79,d_r_c_i_n[r]
        return end

    if direction == "left":
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                d_r_c_i_n.append(i)
        r = int(len(d_r_c_i_n)/2)
        end = d_r_c_i_n[r],0
        return end

    if direction == "right":
        for i in range(len(matrix)):
            if matrix[i][-1] == 0:
                d_r_c_i_n.append(i)
        r = int(len(d_r_c_i_n)/2)
        end = d_r_c_i_n[r],39
        return end
 

def the_matrix(name,start,direction):
    """is responsible for creating a scaled down matrix that represents 
    the maze in the form of 1s for the obstacles and 0s for the path"""  
    mazz = obstacles.get_obstacles()
    ob = []
    for i in mazz:
        if (i[0]%5) == 0 and (i[1]%5) == 0:
            ob.append((int((i[0]+100)/5) , (int((i[1]+200)/5))))
    ob.sort()
    maz = numpy.array(ob)
    matrix = numpy.zeros((80,40),dtype=int)
    try:
        matrix[maz[:,1], maz[:,0]] = 1
    except:
        pass
    m = []
    for i in range(len(matrix)):
        m.append([])
        for j in range(len(matrix[i])):
            m[-1].append(0)
    i,j = start
    m[i][j] = 1

    end = maze_direction(direction,matrix)
    draw_matrix(name, direction, end, matrix ,m ,[])


def draw_matrix(name, direction, end, matrix, m, the_path):
    """calls the function responible for back tracking (finds all possible paths to the end)
    and find the shortest possible path and turns it in to a list of coordinates"""   
    k = 0
    while m[end[0]][end[1]] == 0:
        k += 1
        make_step(k,m,matrix)
    i, j = end
    k = m[i][j]
    the_path = [(i,j)]
    while k > 1:
        if i > 0 and m[i - 1][j] == k-1:
            i, j = i-1, j
            the_path.append((i, j))
            k-=1
        elif j > 0 and m[i][j - 1] == k-1:
            i, j = i, j-1
            the_path.append((i, j))
            k-=1
        elif i < len(m) - 1 and m[i + 1][j] == k-1:
            i, j = i+1, j
            the_path.append((i, j))
            k-=1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
            i, j = i, j+1
            the_path.append((i, j))
            k -= 1
    path_mat = path_matrix(matrix,the_path)
    auto_command(name, direction, the_path, path_mat)


def make_step(k,m,matrix):
    """a recursive function responsible for the actual back tracking"""
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                if i>0 and m[i-1][j] == 0 and matrix[i-1][j] == 0:
                    m[i-1][j] = k + 1
                if j>0 and m[i][j-1] == 0 and matrix[i][j-1] == 0:
                    m[i][j-1] = k + 1
                if i<len(m)-1 and m[i+1][j] == 0 and matrix[i+1][j] == 0:
                    m[i+1][j] = k + 1
                if j<len(m[i])-1 and m[i][j+1] == 0 and matrix[i][j+1] == 0:
                    m[i][j+1] = k + 1


def path_matrix(matrix,the_path):
    """creates a matrix which represents the shortest possible path in the maze"""
    the_path.reverse()
    path_mat = []
    for i in range(len(matrix)):
        path_mat.append([])
        for j in range(len(matrix[i])):
            path_mat[-1].append(0)
    step = 0
    for i in the_path:
        x = i[0]
        y = i[1]
        step = step + 1
        path_mat[-x][y] = step
    l = path_mat[0]
    path_mat.remove(path_mat[0])
    path_mat.append(l)
    return path_mat


def auto_command(name, direction, the_path, path_mat):
    """creates a list containing the movement commands necessary to reach the desired edge"""
    path = []
    mazerun = []
    run = []
    step = 1

    for i in the_path:
        path.append(((i[1]*5 - 100),(i[0]*5 - 200)))

    for _s in range(len(path)):
        for i in range(len(path_mat)):
            for r in range(len(path_mat[i])):
                if path_mat[i][r] == 1 and len(mazerun) == 0:
                    if path_mat[i][r-1] == 2:
                        mazerun.append("left")
                    if path_mat[i][r+1] == 2:
                        mazerun.append("right")
                    if path_mat[i+1][r] == 2:
                        mazerun.append("right")
                        mazerun.append("right")

                if path_mat[i][r] == step and (i < len(path_mat)-1) and (r < len(path_mat[i])-1):
                    if (path_mat[i][r+1] != (step + 1) and path_mat[i][r-1] != (step + 1)) or (r == 0 or r == len(path_mat[i])-2):
                        if(path_mat[i+1][r] == (step + 1) and path_mat[i-1][r] == (step - 1)):
                            mazerun.append("forward 5")
                            step = step + 1
                        if(path_mat[i-1][r] == (step + 1) and path_mat[i+1][r] == (step - 1)):
                            mazerun.append("forward 5")
                            step = step + 1

                    if (path_mat[i+1][r] != (step + 1) and path_mat[i-1][r] != (step + 1)) or (i == 0 or i == len(path_mat)-2):
                        if (path_mat[i][r+1] == (step + 1) and path_mat[i][r-1] == (step - 1)):
                            mazerun.append("forward 5")
                            step = step + 1
                        if (path_mat[i][r-1] == (step + 1) and path_mat[i][r+1] == (step - 1)):
                            mazerun.append("forward 5")
                            step = step + 1

                    if (path_mat[i][r+1] == (step + 1) and path_mat[i][r-1] != (step + 1) and path_mat[i+1][r] == (step - 1)):
                        mazerun.append("right")
                        mazerun.append("forward 5")
                        step = step + 1
                    if (path_mat[i][r-1] == (step + 1) and path_mat[i][r+1] != (step + 1) and path_mat[i-1][r] == (step - 1)):
                        mazerun.append("right")
                        mazerun.append("forward 5")
                        step = step + 1
                    if (path_mat[i+1][r] == (step + 1) and path_mat[i-1][r] != (step + 1) and path_mat[i][r-1] == (step - 1)):
                        mazerun.append("right")
                        mazerun.append("forward 5")
                        step = step + 1
                    if (path_mat[i-1][r] == (step + 1) and path_mat[i+1][r] != (step + 1) and path_mat[i][r+1] == (step - 1)):
                        mazerun.append("right")
                        mazerun.append("forward 5")
                        step = step + 1

                    
                    if (path_mat[i][r-1] == (step + 1) and path_mat[i][r+1] != (step + 1) and path_mat[i+1][r] == (step - 1) ):
                        mazerun.append("left")
                        mazerun.append("forward 5")
                        step = step + 1
                    if (path_mat[i][r+1] == (step + 1) and path_mat[i][r-1] != (step + 1) and path_mat[i-1][r] == (step - 1) ):
                        mazerun.append("left")
                        mazerun.append("forward 5")
                        step = step + 1
                    if (path_mat[i-1][r] == (step + 1) and path_mat[i+1][r] != (step + 1) and path_mat[i][r-1] == (step - 1)):
                        mazerun.append("left")
                        mazerun.append("forward 5")
                        step = step + 1
                    if (path_mat[i+1][r] == (step + 1) and path_mat[i-1][r] != (step + 1) and path_mat[i][r+1] == (step - 1)):
                        mazerun.append("left")
                        mazerun.append("forward 5")
                        step = step + 1

    if direction == "top" or direction == "right":
        mazerun.append("forward 5")

    count = 1
    for i in range(len(mazerun)):
        if i < len(mazerun)-1:
            if mazerun[i] == "forward 5" and mazerun[i] == mazerun[i+1]:  
                count = count + 1
            if mazerun[i] == "forward 5" and (mazerun[i] != mazerun[i+1] or i+1 == len(mazerun)-1 ):
                run.append(f"forward {count*5}")
                count = 1
            if mazerun[i] != "forward 5":
                run.append(mazerun[i])
                count = 1
            if i+1 == len(mazerun)-1 and mazerun[i+1] == "forward 5" and (run[-1] == "right" or run[-1] == "left"):
                run.append("forward 5")

    maze_run_(name, direction, run, path)


def maze_run_(name, direction, mazerun, path):
    """calls the recursive function responsible for playing the list of command to solve the maze
    also determines if the robot has reached the desired edge"""
    the_run(mazerun, "", name, len(mazerun), 0)

    if robot.env == True:
        cord = world.turtle.world.x , world.turtle.world.y
    else:
        cord = world.text.world.x , world.text.world.y

    finish = path[-1]
    if direction == "top":
        finish = finish[1] + 5
        cord = cord[1]
    if direction == "bottom":
        finish = finish[1]
        cord = cord[1]
    if direction == "left":
        finish = finish[0]
        cord = cord[0] 
    if direction == "right":
        finish = finish[0] + 5
        cord = cord[0] 

    if cord == finish :    
        print(f"{name}: I am at the {direction} edge.")
    else:
        print(f"{name}: did not make it to the {direction} edge")


def the_run(mazerun,command, name, nb, r):
    """is a recursive function that plays the list of valid command needed to complete the maze"""
    while r < nb:
        command = mazerun[r]
        # print(f"this is command {command}")
        robot.robot_movement(command,name)
        return the_run(mazerun, command, name, nb, (r+1))
    

