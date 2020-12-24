import math

def get_area(shape):
    shape=shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    
    
    elif shape =="triangle":
        tringle_area()

    else:
    
        print("please enter a right shape")



def rectangle_area():
    lenght=float(input("please enter the lenght of the rectangle: "))
    width = float(input("please enter the width of the rectangle: "))
    area = width * lenght
    print("area of the rectangle is {}".format(area))

def tringle_area():
    base=float(input("enter the base of the tringle : "))
    height=float(input("enter the height of the triangle : "))
    area = (base * height) / 2
    print("the area of the triangle is : {}".format(area))


def circle_area():
    radius =float(input("Please enter the radius of the circle: "))
    area= math.pi * (math.pow(radius,2))
    print("the area of the circle is : {}".format(area))


def main():
    shape_type=input("please enter the shape of the desired area: ")
    get_area(shape_type)

main()
