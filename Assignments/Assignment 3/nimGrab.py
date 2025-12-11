"""
Muhammad Muhamedjonov, 10-10-2025
Assignment 3 - This is the classic game of NIM called NIMGRAB!
"""

import random

def print_header():
    print()
    print("NIMGRAB!")
    print("By Muhammad Muhamedjonov")
    print("COM S 127 section 02")
    print()

def show_rules():
    rules = f"""
Rules of NIMGRAB!

- Objective: Players alternate removing items from a row. The player who takes
  the last item loses.
- At the start of the game there are N items in a row.
- On a turn a player must take between X = 1 and Y = 3 or you can always customize muber of items taking.
- A player cannot take more items than currently remain.
- In 1-player mode the human goes first. In 2-player mode whoever is chosen goes first.
"""
    print(rules)

def run_bot():
    n = random.randrange(7, 31)
    x = random.randrange(1, 3)
    y = random.randrange(x + 2, x + 3)
    print("Do you want to [c]ustomize initials or set it by [d]efault?:")
    s = str(input())
    if(s == "c"):
        n = int(input("Number of items: "))
        x = int(input("Minimum number of items for taking: "))
        y = int(input("Maximum number of items for taking: "))
    
    print("Game has started.")
    t = 0
    while(n >= x):
        print()
        s = ""
        for i in range(n):
            s += "| "
        print(f"Items left: {n}")
        print(s)
        print()

        a = -1
        if(t % 2 == 0):
            print("Your turn")
            while(a < x or a > y or a > n):  
                a = int(input(f"How many items do you want to take [{x} - {y}]?: "))
                if(a < x or a > y or a > n):
                    print("Try again")
        if(t % 2 == 1):
            a = random.randrange(x, min(y + 1, n + 1))
            for i in range(x, y + 1):
                if(n - i >= x and (n - i) < (2 * x) and n - i <= y):
                    a = i
                    break
            s = ""
            if(a > 1):
                s = "s"
            print(f"Computer takes {a} item{s}")
        n -= a
        t += 1
    if(t % 2 == 0):
        print("You won! Game is over.")
    if(t % 2 == 1):
        print("Computer won! Game is over.")
            

def run_human():
    n = random.randrange(7, 31)
    x = random.randrange(1, 3)
    y = random.randrange(x + 2, x + 3)
    print("Do you want to [c]ustomize initials or set it by [d]efault?:")
    s = str(input())
    if(s == "c"):
        n = int(input("Number of items: "))
        x = int(input("Minimum number of items for taking: "))
        y = int(input("Maximum number of items for taking: "))
    
    print("Game has started.")
    t = 0
    while(n >= x):
        s = ""
        for i in range(n):
            s += "| "
        print(f"Items left: {n}")
        print(s)
        print()

        a = -1
        if(t % 2 == 0):
            print("Player-1")
        if(t % 2 == 1):
            print("Player-2")
        while(a < x or a > y or a > n):  
            a = int(input(f"How many items do you want to take [{x} - {y}]?: "))
        n -= a
        t += 1
    if(t % 2 == 0):
        print("Player-1 won! Game is over.")
    if(t % 2 == 1):
        print("Player-2 won! Game is over.")
    return

            

def main():
    print_header()
    while(True):
        print("Do you want to [p]lay, read the [r]ules, or [q]uit?:")
        s = str(input())

        if(s == "q"):
            break

        if(s == "r"):
            show_rules()
            continue

        if(s == "p"):
            print("Do you want to play in [1] - player mode(against a computer) or in [2] - player mode(against another human), or do you want to [q]uit?:")
            s = str(input())
            if(s == "q"):
                break
            if(s == "1"):
                run_bot()
            if(s == "2"):
                run_human()

    print("You quit the game. Bye!")

if(__name__ == "__main__"):
    main()