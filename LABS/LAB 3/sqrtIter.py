"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, find approximate square root of x with n iterations in python using functions
"""

def sqrtIter(x, iter):
    y = (x + 1) / 2
    for i in range(iter):
        y = (x / y + y) / 2
    return y

def main():
    # return square root of x
    x = int(input("x: "))
    iter = int(input("iterations: "))
    answer = sqrtIter(x, iter)
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()
