"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, example of how to find voltage using current and resistance in python using functions
URL: byjus.com/physics/unit-of-voltage
Author: N/A
Date posted: N/A
"""

def calculateVoltage(current, resistance):
    # calculate voltage
    voltage = current * resistance
    return voltage

def main():
    current = float(input("current: "))
    resistance = float(input("resistance: "))
    voltage = calculateVoltage(current, resistance)
    print(f"Voltage equals: {voltage}")

if __name__ == "__main__":
    main()