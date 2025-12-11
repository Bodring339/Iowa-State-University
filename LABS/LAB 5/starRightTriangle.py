"""
Muhammad Muhamedjonov, 08.10.2025, 
LAB 5,
"""

def starRightTriangle(n):
    for i in range (1, n + 1):
        s = ""
        for j in range (1, i + 1):
            s += "*"
        print(s)


def main():
    num = int(input("Number: "))
    starRightTriangle(num)


if __name__ == "__main__":
    main()
