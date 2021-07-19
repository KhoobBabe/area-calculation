import area_module              #this contains the functions to calculate ..
                                #..the area of triangle, circle, rectangle

#function for the area of cylinder
def cylinder():
    rad_1 = float(input("Enter the radius of base: "))
    h = float(input("Enter the height: "))

    area_cyl = 2 * 3.14159 * rad_1 * (rad_1 + h)

    print("The area of cylinder is: ", area_cyl, "\n")


#the options are given the start
print("The shapes whose area you can calculate are:-")
print("Triangle")
print("Circle")
print("Rectngle")
print("Cylinder")
print("Write 'quit' to end the program\n")

name = ""
#while loop to prompt the user to add more shapes
while name != "b": 
    name = input("enter the name of the shape: ")

    if name == 'triangle':
        area_module.triangle()
        
    elif name == 'circle':
        area_module.circle()
        
    elif name == 'rectangle':
        area_module.rectangle()
        
    elif name == 'cylinder':
        cylinder()

    elif name == 'quit':
        #closes the program with a message
        print("Program closed")
        break

    else:
        #if the input is except the options provided
        print("Enter from the above mentioned shapes")
        
    
