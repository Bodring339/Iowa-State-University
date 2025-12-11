"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, return product of 'a' random integers chosen from interval [b, c) in python using functions
"""

import random

def randomProduct(a, b, c):
    answer = 1
    for i in range (0, a):
        r = random.randrange(b, c + 1)
        answer *= r
    return answer

def main():
    # Return product of 'a' random integers chosen from interval [b, c)
    a = int(input("a: " ))
    b = int(input("b: " ))
    c = int(input("c: " ))
    if a <= 0 or b > c:
        print(f"Error")
        return
    answer = randomProduct(a, b, c)
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()
