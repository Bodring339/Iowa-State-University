"""
Muhammad Muhamedjonov, 09.10.2025, 
LAB 2, example of how to find annual percentage rate using interest charges, fees, loan amount and number of days in term in python
URL: keysavingsbank.com/mortgage-interest-rates/
Author: N/A
Date posted: N/A
"""
interest_charges = float(input("interest charges: "))
fees = float(input("fees: "))
loan_amount = float(input("loan amount: "))
days_in_term = float(input("days in term: "))
apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100
print(f"Annual Percentage Rate equals: {apr}")