#function for the area of triangle
def triangle():
    base = float(input("Enter the base length: "))
    hei = float(input("Enter the height: "))

    area_tri = 0.5 * base * hei

    print("The area of the triangle is: ", area_tri, "\n")
    

    


#function for the area of rectangle
def rectangle():
    length = float(input("Enter the the length: "))
    width = float(input("Enter the width: "))

    area_rec = length * width
    print("The area of the rectangle is: ", area_rec, "\n")
    





#function for the area of circle
def circle():
    radius = float(input("Enter the radius: "))

    area_circ = 3.14159 * (radius**2)

    print("The area of the circle is: ", area_circ, "\n")
    
