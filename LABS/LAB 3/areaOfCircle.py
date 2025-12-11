"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, example of how to find area of a circle in python using functions
URL: byjus.com/maths/area-of-circle
Author: N/A
Date posted: N/A
"""

import math

def areaOfCircle(radius):
    # calculate area
    area = math.pi * (radius ** 2)
    return area

def main():
    radius = float(input("Please enter the radius: "))
    area = areaOfCircle(radius)
    print(f"Area of circle is: {area}")

if __name__ == "__main__":
    main()