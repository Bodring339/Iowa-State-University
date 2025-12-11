"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, example of how to find annual percentage rate using interest charges, fees, loan amount and number of days in term in python using functions
URL: keysavingsbank.com/mortgage-interest-rates/
Author: N/A
Date posted: N/A
"""

def annualPercentageRate(interest_charges, fees, loan_amount, days_in_term):
    # calculate apr
    apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100
    return apr

def main():
    interest_charges = float(input("interest charges: "))
    fees = float(input("fees: "))
    loan_amount = float(input("loan amount: "))
    days_in_term = float(input("days in term: "))
    apr = annualPercentageRate(interest_charges, fees, loan_amount, days_in_term)
    print(f"Annual Percentage Rate equals: {apr}")

if __name__ == "__main__":
    main()