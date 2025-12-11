"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, example of how to find accrued amount in python using functions
URL: byjus.com/maths/compound-interest/
Author: N/A
Date posted: N/A
"""

def compoundAmount(principal, rate, number_compounds, time):
    # calculate accrued_amount
    accrued_amount = principal * (1 + (rate/100) / number_compounds)**(number_compounds* time)
    return accrued_amount

def main():
    principal = float(input("principal: "))
    rate = float(input("rate: "))
    number_compounds = float(input("number compounds: "))
    time = float(input("time: "))
    accrued_amount = compoundAmount(principal, rate, number_compounds, time)
    print(f"Accrued Amount equals: {accrued_amount}")

if __name__ == "__main__":
    main()