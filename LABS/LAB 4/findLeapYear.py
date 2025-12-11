"""
Muhammad Muhamedjonov, 01.10.2025, 
LAB 4, code of how to define if the year is leap or not in python using functions
"""

def findLeapYear(y):
    return ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))

def main():
    y = int(input("Year: "))
    ch = findLeapYear(y)
    if(ch == True):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
