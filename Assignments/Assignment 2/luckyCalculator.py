# Muhammad Muhamedjonov, 11-04-2025
# Assignment 2, COM S 1270 - 02 (LAB K)
#
# This is the code of calculator that can do 7 different operations & generate a lucky number

import random

def main():

    print("Lucky Calculator!")
    print()

    print("By: Muhammad Muhamedjonov")
    print("[COM S 127 02]")
    print()

    print("What would you like to do?")
    print()

    ar = ["+", "-", "*", "**", "//", "%", "/"]
    c = ""
    res = 0

    t = str(input("[c]alculator, [l]ucky number, [q]uit: "))

    if(t == "q"):
        print("You quit the game, Goodbye!")
        return
    
    elif(t == "c"):
        c = str(input("Please Choose a Calculation [+], [-], [*], [/], [//], [%], [**]: "))
        if(c != "+" and c != "-" and c != "*" and c != "/" and c != "//" and c != "%" and c != "**"):
            print("ERROR: Calculator did not understand your input. Please try again.")
    elif(t == "l"):
        c = ar[random.randint(0, 6)]
    else:
        print("ERROR: Calculator did not understand your input. Please try again.")
        return

    a = int(input("Please Enter Your First Integer: "))
    b = int(input("Please Enter Your Second Integer: "))

    if(t == "l"):
        a *= random.randint(1, 2)
        b += random.randint(1, 3)
        
    if(b == 0):
        c = ar[random.randint(0, 3)]

    if(b == 0 and (c == "/" or c == "//" or c == "%")):
        print("ERROR. There's invalid input. Please try again")
        return
    res = a + b
    if(c == "-"):
        res = a - b
    elif(c == "*"):
        res = a * b
    elif(c == "/"):
        res = a / b
    elif(c == "//"):
        res = a / b
    elif(c == "%"):
        res = a % b
    elif(c == "**"):
        res = a ** b
    
    if(t == "c"):
        print(f"The result of your calculation is: {res}")
    else:
        print(f"Your lucky number is: {res}")


if(__name__ == "__main__"):
    main()