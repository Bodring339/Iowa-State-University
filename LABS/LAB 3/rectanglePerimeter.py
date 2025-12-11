"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, example of how to find perimeter of a rectangle in python using functions
URL: byjus.com/maths/perimeter-of-rectangle
Author: N/A
Date posted: N/A
"""

def rectanglePerimeter(base, height):
    # calculate perimeter
    perimeter = 2 * (base + height)
    return perimeter

def main():
    base = float(input("Base: "))
    height = float(input("Height: "))
    perimeter = rectanglePerimeter(base, height)
    print(f"Perimeter of rectangle is: {perimeter}")

if __name__ == "__main__":
    main()