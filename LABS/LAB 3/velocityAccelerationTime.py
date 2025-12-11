"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, example of how to find final velocity using initial velocity, acceleration and time in python using functions
URL: byjus.com/physics/velocity
Author: N/A
Date posted: N/A
"""

def velocityAccelerationTime(initial_velocity, acceleration, time):
    # calculate final_velocity
    final_velocity = initial_velocity + (acceleration * time)
    return final_velocity

def main():
    initial_velocity = float(input("initial velocity: "))
    acceleration = float(input("acceleration: "))
    time = float(input("time: "))
    final_velocity = velocityAccelerationTime(initial_velocity, acceleration, time)
    print(f"Final velocity equals: {final_velocity}")

if __name__ == "__main__":
    main()