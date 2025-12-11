"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 4, 
"""


def annualPercentageRate(interest_charges, fees, loan_amount, days_in_term):
    # calculate apr
    apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100
    return apr

def compoundAmount(principal, rate, number_compounds, time):
    # calculate accrued_amount
    accrued_amount = principal * (1 + (rate/100) / number_compounds)**(number_compounds* time)
    return accrued_amount