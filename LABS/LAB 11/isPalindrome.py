# Muhammad Muhamedjonov
# LAB 11 (K), 11-10-2025
# isPalindrome few approaches

def isPalindromeIterative(s):
    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True


def isPalindromeRecursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    
    return isPalindromeRecursive(s[1:-1])


def main():
    s = input("String: ")
    print(f"Iterative result {isPalindromeIterative(s)}")
    print(f"Recursive result {isPalindromeRecursive(s)}")


if __name__ == "__main__":
    main()
