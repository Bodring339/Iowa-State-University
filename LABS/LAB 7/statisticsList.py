"""
Muhammad Muhamedjonov, 10.28.2025, 
LAB 7, Code of how to find a mean and median of an array
"""

import random

def generateInput():
    n = random.randint(200, 501)
    a = [0] * n
    for i in range(n):
        a[i] = random.randint(1, 2001)
    return a

def findMean(a):
    res = 0
    for i in a:
        res += i
    res /= len(a)
    return res

def findMedian(a):
    n = len(a)
    a.sort()
    # res = 0
    # if(n % 2 == 0):
    #     res = (a[n // 2] + a[n // 2 - 1]) / 2
    # else:
    #     res = a[n // 2]
    # print(res)
    return (a[n // 2] + a[(n - 1) // 2]) / 2


def main():
    a = generateInput()
    # print(f"Random array: {a}")
    x = findMean(a)
    y = findMedian(a)
    print(f"Mean: {x}")
    print(f"Median: {y}")

if(__name__ == "__main__"):
    main()