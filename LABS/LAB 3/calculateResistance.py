"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, example of how to find resistance using voltage and current in python using functions
URL: byjus.com/physics/unit-of-resistance
Author: N/A
Date posted: N/A
"""

def calculateResistance(voltage, current):
    # calculate resistance
    resistance = voltage / current
    return resistance

def main():
    voltage = float(input("voltage: "))
    current = float(input("current: "))
    resistance = calculateResistance(voltage, current)
    print(f"Resistance equals: {resistance}")

if __name__ == "__main__":
    main()