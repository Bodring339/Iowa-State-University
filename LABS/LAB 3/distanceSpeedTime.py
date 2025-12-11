"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, example of how to find distance using speed and time in python using functions
URL: byjus.com/govt-exams/speed-time-distance
Author: N/A
Date posted: N/A
"""

def distanceSpeedTime(speed, time):
    # calculate distance
    distance = speed * time
    return distance

def main():
    speed = float(input("speed: "))
    time = float(input("time: "))
    distance = distanceSpeedTime(speed, time)
    print(f"Distance equals: {distance}")

if __name__ == "__main__":
    main()