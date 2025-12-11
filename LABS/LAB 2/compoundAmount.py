"""
Muhammad Muhamedjonov, 09.10.2025, 
LAB 2, example of how to find accrued amount in python
URL: byjus.com/maths/compound-interest/
Author: N/A
Date posted: N/A
"""
principal = float(input("principal: "))
rate = float(input("rate: "))
number_compounds = float(input("number compounds: "))
time = float(input("time: "))
accrued_amount = principal * (1 + (rate/100) / number_compounds)**(number_compounds* time)
print(f"Accrued Amount equals: {accrued_amount}")