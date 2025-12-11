"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, example of how to find current using voltage and resistance in python using functions
URL: byjus.com/physics/unit-of-resistance
Author: N/A
Date posted: N/A
"""

def calculateCurrent(voltage, resistance):
    # calculate current
    current = voltage / resistance
    return current

def main():
    voltage = float(input("voltage: "))
    resistance = float(input("resistance: "))
    current = calculateCurrent(voltage, resistance)
    print(f"Current equals: {current}")

if __name__ == "__main__":
    main()