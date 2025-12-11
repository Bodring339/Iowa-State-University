"""
Muhammad Muhamedjonov, 09.10.2025, 
LAB 2, example of how to find final velocity using initial velocity, acceleration and time in python
URL: byjus.com/physics/velocity
Author: N/A
Date posted: N/A
"""
initial_velocity = float(input("initial velocity: "))
acceleration = float(input("acceleration: "))
time = float(input("time: "))

final_velocity = initial_velocity + (acceleration * time)
print(f"Final velocity equals: {final_velocity}")