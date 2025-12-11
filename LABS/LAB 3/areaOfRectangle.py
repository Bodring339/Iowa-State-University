"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, example of how to find area of a rectangle in python using functions
URL: byjus.com/maths/area-of-rectangle
Author: N/A
Date posted: N/A
"""

def areaOfRectangle(base, height):
    # calculate area
    area = base * height
    return area

def main():
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = areaOfRectangle(base, height)
    print(f"Area of rectangle is: {area}")

if __name__ == "__main__":
    main()