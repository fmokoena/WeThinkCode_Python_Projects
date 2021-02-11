

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ").lower()
    if shape.lower() == "pyramid":
        return shape
    elif shape.lower() == "square":
        return shape
    elif shape.lower() == "triangle":
        return shape
    elif shape.lower() == "rhombus":
        return shape  
    elif shape.lower() == "trapezium":
        return shape
    elif shape.lower() == "down pyramid":
        return shape
    else:
        return get_shape()
     

# TODO: Step 1 - get height (it must be int!)
def get_height():
    try :
        height = int(input("Height?: "))
        return height
    except:
        return get_height()
        


# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == False:
        for i in range(0, height):
            print(" "* (height -i -1)+'*'*(2*i+1))
    elif outline == True:
        for i in range(0, height):
            if i == 0 or i == height-1:
                print (" "*(height - i - 1)+ "*"*(2*i+1))
            else:
                print(" "* (height - i - 1)+"*"+" "*(2*i-1)+"*")

        
# TODO: Step 3
def draw_square(height, outline):
    if outline == False:
        for i in range(0, height):
           print("*"* height)
    elif outline == True:
        for i in range(0,height):
           if i == 0 or i == height - 1:
            print("*"* height)
           else:
            print('*'+' '*(height-2)+"*")
 
        
# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        for i in range(1, height+1):
            print("*"*i)
            
    elif outline == True:
        for i in range (1, height+1):
            if i <= 2 or i == height :
                print("*"*i)
            else:
                print("*" + " "* (i - 2) + "*")

# TODO: Steps 6
def draw_rhombus(height, outline):
    if outline == False:
        for i in range (0,(height+1)):
            print(" "* (height-i) + "*"* height)

    elif outline == True:
        for i in range(0, height):
            if i == 0 or i == (height - 1) :
                print(" "* (height-i) + "*"* height)
            else:
                print(" "* (height-i)+"*"+" "* (height-2)+"*" )
            
def draw_trapezium(height, outline):
    if outline == False:
       for i in range(0,height):
            print(" "* (height -i -1)+'*'*(2*(i+height))) 
    elif outline == True:
        for i in range(0, height):
            if i == 0 or i == (height - 1) :
                print(" "* (height-i -1) + "*"*( 2 *(i+height)))
            else:
                print(" "* (height-i -1)+"*"+" "* (2*(i+height-1))+"*")

def draw_down_pyramid(height, outline):
    if outline == False:
        for i in range(0,height):
            print(" "* (height +i -1)+'*'*(2*(height-i)-1))
    elif outline == True:
        for i in range(0, height):
            if i == 0 or i == (height - 1) :
                print(" "* (height +i -1)+'*'*(2*(height-i)-1))
            else:
                print(" "* (height + i - 1)+"*"+" "*(2*(height-i)-3)+"*")

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid" :
        draw_pyramid(height, outline)
    elif shape == "square" :
        draw_square(height, outline)
    elif shape == "triangle" :
        draw_triangle(height, outline)
    elif shape == "rhombus":
        draw_rhombus(height, outline)
    elif shape == "trapezium":
        draw_trapezium(height, outline)
    elif shape == "down pyramid":
        draw_down_pyramid(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("outline only ? (y/n) : ")
    if (outline == "y" or outline == "Y"):
        #return outline
        return True
    elif(outline == "n" or outline == "N"):
        #return outline
        return False
    else:
        return get_outline()



if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

