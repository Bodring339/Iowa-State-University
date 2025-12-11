"""
Muhammad Muhamedjonov, 10.28.2025, 
LAB 7, Rotate elements ofthe list
"""

def makel():
    a = []
    while(True):
        s = str(input())
        if(s == "*"):
            break
        a.append(int(s))
    return a

def rotateList(a, rot):
    n = len(a)
    rot %= n
    b = []
    for i in range(n - rot, n):
        b.append(a[i])
    for i in range(n - rot):
        b.append(a[i])
    return b

def main():
    a = makel()
    rot = int(input("rotate: "))
    b = rotateList(a, rot)
    print(b)

if(__name__ == "__main__"):
    main()