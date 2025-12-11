"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 4, 
"""


def calculateCurrent(voltage, resistance):
    # calculate current
    current = voltage / resistance
    return current

def calculateResistance(voltage, current):
    # calculate resistance
    resistance = voltage / current
    return resistance

def calculateVoltage(current, resistance):
    # calculate voltage
    voltage = current * resistance
    return voltage

