"""
Muhammad Muhamedjonov, 08.10.2025, 
LAB 5,
"""

def studentLoanAmortization(p, ir, n):
    x = int(max(len(str(p)), len(str(ir)), len(str(n))))
    sp = ""
    for i in range(0, x):
        sp += " "
    sp = max(sp, "    ")
    prnt = "Period" + sp + "Total Payment Due" + sp + "Computed Interest" + sp + "Principal Due" + sp +  "Principal Balance"
    print(prnt)

    mir = ir / 12

    # computed_interest = 
    # principal_due = 

    principal_balance = p
    totpayment = (mir * ((1 + mir) ** n)) / (((1 + mir) ** n) - 1) * p
    print(totpayment)
    # for period in range (1, n * 12 + 1):



def main():
    principal = float(input("Please Input the Principal: "))
    yearlyInterestRate = float(input("Please Input the Yearly Interest: "))
    numberOfYears = int(input("Please Input the Number of Years: "))
    studentLoanAmortization(principal, yearlyInterestRate, numberOfYears)


if __name__ == "__main__":
    main()
