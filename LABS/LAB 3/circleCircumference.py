"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, example of how to find circumference of a circle in python using functions
URL: byjus.com/maths/circumference-of-a-circle
Author: N/A
Date posted: N/A
"""

import math 

def circleCircumference(radius):
    # calculate circumference
    circumference = 2 * math.pi * radius
    return circumference

def main():
    radius = float(input("radius: "))
    circumference = circleCircumference(radius)
    print(f"Circumference of circle is: {circumference}")

if __name__ == "__main__":
    main()