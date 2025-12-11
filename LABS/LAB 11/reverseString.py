# Muhammad Muhamedjonov
# LAB 11 (K), 11-10-2025
# reverseString few approaches

def reverseIterative(s):
    sr = ""
    for c in s:
        sr = c + sr
    return sr

def reverseRecursive(s):
    if len(s) <= 1:
        return s
    return reverseRecursive(s[1:]) + s[0]


def main():
    s = input("String: ")
    print(f"Iterative result {reverseIterative(s)}")
    print(f"Recursive result {reverseRecursive(s)}")


if __name__ == "__main__":
    main()
