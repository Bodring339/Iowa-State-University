"""
Muhammad Muhamedjonov, 10.28.2025, 
LAB 7, finding minimum and maximum from the list
"""

def makel():
    a = []
    while(True):
        s = str(input())
        if(s == "*"):
            break
        a.append(int(s))
    return a

def findMin(a):
    mn = 0
    ok = 0
    for i in a:
        if(ok == 0 or i < mn):
            mn = i
        ok = 1
    return mn

def findMax(a):
    mx = 0
    ok = 0
    for i in a:
        if(ok == 0 or i > mx):
            mx = i
        ok = 1
    return mx

def main():
    a = makel()
    mn = findMin(a)
    mx = findMax(a)
    print(f"Minimum: {mn}")
    print(f"Maximum: {mx}")

if(__name__ == "__main__"):
    main()