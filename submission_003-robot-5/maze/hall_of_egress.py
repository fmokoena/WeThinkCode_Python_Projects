
def get_obstacles():
    """creates a list with the coordinates of all the obstacles that make the main maze"""
    maze = [] 
    for i in range(-100,100):
        if (i%5) == 0:
            if i in range(-30,25): 
                maze.append((i, -95))
                maze.append((i, 90))
            if i in range(-90,80):
                maze.append((-30,i))
            if i in range(-80,90):
                maze.append((25,i))
            if i in range(-20,15): 
                maze.append((i, -65))
                maze.append((i, 60))
            if i in range(-50,60):
                maze.append((-20,i))
            if i in range(-60,50):
                maze.append((15,i))
            if i in range(-10,5): 
                maze.append((i, -35))
                maze.append((i, 30))
            if i in range(-25,30):
                maze.append((-10,i))
            if i in range(-30,25):
                maze.append((5,i))

    for i in range(-100,100):
        if (i%5) == 0:
            if (i in range(-40,-5) or i in range(5,35)):
                maze.append((i,105)) 
                maze.append((i,-110))
            if (i in range(-50,45)):  
                maze.append((i,120)) 
                maze.append((i,-125))
            if (i in range(-60,-5) or i in range(5,55)):
                maze.append((i,135)) 
                maze.append((i,-140))
            if (i in range(-70,65)):  
                maze.append((i,150)) 
                maze.append((i,-155))
            if (i in range(-75,-5) or i in range(5,70)):
                maze.append((i,165)) 
                maze.append((i,-170))
            if (i in range(-80,75)):  
                maze.append((i,180)) 
                maze.append((i,-185))
            if (i in range(-100,-5) or i in range(5,95)):
                maze.append((i,195)) 
                maze.append((i,-200)) 
                
    for k in range(-200,200):
        if (k%5) == 0:
            if (k in range(-105,-5) or k in range(5,105)):
                maze.append((-40,k)) 
                maze.append((35,k))
            if (k in range(-110 ,110)):  
                maze.append((-50,k)) 
                maze.append(( 45,k))
            if (k in range(-135,-5) or k in range(5,135)):
                maze.append((-60,k)) 
                maze.append((55,k))
            if (k in range(-140,140)):  
                maze.append((-70,k)) 
                maze.append(( 65,k))
            if (k in range(-170,-5) or k in range(5,170)):
                maze.append((-80,k)) 
                maze.append((75,k))
            if (k in range(-185,185)):  
                maze.append((-90,k)) 
                maze.append(( 85,k))
            if (k in range(-200,-5) or k in range(5,200)):
                maze.append((-100,k)) 
                maze.append((95, k)) 
    maze = list(dict.fromkeys(maze))
    return maze 