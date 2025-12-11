"""
Muhammad Muhamedjonov, 08.10.2025, 
LAB 5,
"""

def numberPyramid(n):
    sz = int(n * 2 - 1)
    st = int((sz + 1) / 2) + 1
    for i in range (1, n + 1):
        st = st - 1
        st = max(st, 1)
        s = ""
        for j in range (st):
            s = s + " "
        for j in range(1, i + 1):
            s = s + str(j) + " "
        print(s)


def main():
    num = int(input("Number: "))
    numberPyramid(num)


if __name__ == "__main__":
    main()
