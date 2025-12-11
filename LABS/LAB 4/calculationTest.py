"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 4, 
"""

import myShapes
import myPhysics
import myOhmsLaw
import myFinances

def main():
    b = True
    while b:
        print("Which of the following functions do you want to use? Type:\n")
        print(" 'S' if you want to use myShapes.py\n")
        print(" 'P' if you want to use myPhysics.py\n")
        print(" 'O' if you want to use myOhmsLaw.py\n")
        print(" Or 'F' if you want to use myFinances.py\n")
        print(" Type 'X' if you just want to quit\n")
        ch = str(input(""))
        if(ch == "X"): 
            b = False 
            continue
        
        print("What do you want to find? Type:\n")
        if(ch == "S"):
            print(" AR if you want to find area of reactangle\n")
            print(" RP if you want to find rectangle perimeter\n")
            print(" AC if you want to find are of circle\n")
            print(" CC if you want to find circle circumference\n")
            t = str(input(""))
            if(t == "AR"):
                base = float(input("Base: "))
                height = float(input("Height: "))
                print("The answer is: ")
                print({myShapes.areaOfRectangle(base, height)})
            elif(t == "RP"):
                base = float(input("Base: "))
                height = float(input("Height: "))
                print("The answer is: ")
                print({myShapes.rectanglePerimeter(base, height)})
            elif(t == "AC"):
                radius = float(input("Radius: "))
                print("The answer is: ")
                print({myShapes.areaOfCircle(radius)})
            elif(t == "CC"):
                radius = float(input("Radius: "))
                print("The answer is: ")
                print({myShapes.circleCircumference(radius)})

        elif(ch == "P"):
            print(" D if you want to find distance\n")
            print(" FV if you want to find final velocity\n")
            t = str(input(""))
            if(t == "D"):
                speed = float(input("Speed: "))
                time = float(input("Time: "))
                print("The answer is: ")
                print({myPhysics.distanceSpeedTime(speed, time)})
            elif(t == "FV"):
                initial_velocity = float(input("initial velocity: "))
                acceleration = float(input("acceleration: "))
                time = float(input("time: "))
                print("The answer is: ")
                print({myPhysics.velocityAccelerationTime(initial_velocity, acceleration, time)})

        elif(ch == "O"):
            print(" C if you want to find current\n")
            print(" R if you want to find resistance\n")
            print(" V if you want to find voltage\n")
            t = str(input(""))
            if(t == "C"):
                resistance = float(input("Resistance: "))
                voltage = float(input("Voltage: "))
                print("The answer is: ")
                print({myOhmsLaw.calculateCurrent(resistance, voltage)})
            elif(t == "R"):
                current = float(input("Current: "))
                voltage = float(input("Voltage: "))
                print("The answer is: ")
                print({myOhmsLaw.calculateResistance(current, voltage)})
            elif(t == "V"):
                current = float(input("Current: "))
                resistance = float(input("Resistance: "))
                print("The answer is: ")
                print({myOhmsLaw.calculateVoltage(current, resistance)})

        elif(ch == "F"):
            print(" APR if you want to find Annual Percentage Rate\n")
            print(" AA if you want to find Accrued Amount\n")
            t = str(input(""))
            if(t == "APR"):
                interest_charges = float(input("interest charges: "))
                fees = float(input("fees: "))
                loan_amount = float(input("loan amount: "))
                days_in_term = float(input("days in term: "))
                print("The answer is: ")
                print({myFinances.annualPercentageRate(interest_charges, fees, loan_amount, days_in_term)})
            elif(t == "AA"):
                principal = float(input("principal: "))
                rate = float(input("rate: "))
                number_compounds = float(input("number compounds: "))
                time = float(input("time: "))
                print("The answer is: ")
                print({myFinances.compoundAmount(principal, rate, number_compounds, time)})
    
if __name__ == "__main__":
    main()