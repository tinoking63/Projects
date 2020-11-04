

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ")
    shape = shape.lower()
    if (shape == "pyramid" or shape == "square" or shape == "triangle" or shape == "rombus" or shape == "rectangle"or shape == "isosceles"):
        return shape
    else:
        return get_shape()
  


# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
        height = input("Height?: ")
        # height = int(height)
        if height.isnumeric() and height:
            height = int(height)
            if height in range (0,81):
                break
    return height

   

# TODO: Step 2
def draw_pyramid(height, outline):
     if outline == False:
         for row in range(1, height + 1):
            n = (row * 2) - 1
            h = (height)
            print(" "*(h-row)+"*"*n)
            #height -= 1

     else:
        for row in range (0,height):
            for col in range (1,height - row):
                print(" ", end = "")
            for col in range (0,2 * row + 1):
                if (col == 0 or col == 2 * row or row == (height - 1)):
                    print("*", end = "")
                else:
                    print(" ", end = "")
            print()



# TODO: Step 3
def draw_square(height, outline):
    if outline == False:
        for row in range(0, height):
            for col in range(height):
                if((row >= 0 or row <= height) and (col >= 0 or col <= height)):
                    print("*", end = "")
                else:
                    print(end = " ")
            print()
    else:
        for row in range(0, height):
            for col in range(height):
                if (row == 0 or row == height-1 or col == 0 or col == height-1):
                    print("*", end = "")
                else:
                    print(" ",end = "")
            print()
        # print('square')

# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        for row in range(0,height):
            for col in range(0, row + 1):
                print("*", end = "")
            print()
    else:
        for row in range(0,height):
            for col in range (0, row + 1):
                if (col == 0 or row == height-1 or row == col):
                    print("*", end = "")
                else:
                    print(end = " ")
            print()
        # print('triangle')

def draw_rombus(height,outline):
    if outline == False:
        n = height
        for row in range(0,height):  
            print(" "*n, "*"*height)
            n -= 1

    else:
        for row in range (0,height):
            for col in range (height - row -1):
                    print(" ", end = "")
            for col in range (height):
                if (col == 0  or row == height-1 or col == height-1 or row == 0):
                        print("*", end = "")
                else:
                    print(" ", end = "")
            print()
    print("rombus")

def draw_rectangle(height,outline):
    if outline == False:
        for row in range(0, height):
            for col in range(height*5):
                if((row >= 0 or row <= height) and (col >= 0 or col <= height)):
                    print("*", end = "")
                else:
                    print(end = " ")
            print()
    else:
        for row in range(0, height):
            for col in range(height*5):
                if (row == 0 or row == height-1 or col == 0 or col == (height*5)-1):
                    print("*", end = "")
                else:
                    print(" ",end = "")
            print()

def draw_isosceles(height,outline):
    if outline == False:
        for row in range (0,height):
            for col in range(0,row+1):
                print("*",end = "")
            print()
        for row in range(height,0,-1):
            for col in range(0, row):
                print("*", end = "")
            print()
    else:
        for row in range(0,height):
            for col in range (0, row + 1):
                if (col == 0   or row == col):
                    print("*", end = "")
                else:
                    print(end = " ")
            print()
        for row in range(height,0,-1):
            for col in range (0, row + 1):
                if (col == 0  or row == col):
                    print("*", end = "")
                else:
                    print(end = " ")
            print()

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "rombus":
        draw_rombus(height,outline)
    elif shape == "rectangle":
        draw_rectangle(height,outline)
    elif shape == "isosceles":
        draw_isosceles(height,outline)

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (y/N):")
    outlne = str(outline)
    if outline == "Y" or outline == "y":
        return True
    elif outline == "N" or outline == "n":
        return False 

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

