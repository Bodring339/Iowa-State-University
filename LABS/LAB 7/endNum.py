"""
Muhammad Muhamedjonov, 10.28.2025, 
LAB 7, put all the elements equal [num] in the end of array
"""

def makel():
    a = []
    while(True):
        s = str(input())
        if(s == "*"):
            break
        a.append(int(s))
    return a

def endNum(a, num):
    n = len(a)
    b = []
    cnt = 0
    for i in range(n):
        if(a[i] == num):
            cnt += 1
        else:
            b.append(a[i])
    for i in range(cnt):
        b.append(num)
    return b

def main():
    a = makel()
    num = int(input("Num: "))
    b = endNum(a, num)
    print(b)

if(__name__ == "__main__"):
    main()