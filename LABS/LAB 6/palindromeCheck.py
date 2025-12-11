"""
Muhammad Muhamedjonov, 10.15.2025, 
LAB 6, Checking if the string is a palindrome in python
"""

import reverseString

def palindromeCheckV1(s):
    rs = reverseString.reverseStringV1(s)
    if(s == rs):
        return "YES the string is palindrome"
    else:
        return "NO the string is not palindrome"

def palindromeCheckV2(s):
    ok = True
    sz = len(s)
    for i in range(sz):
        if(s[i] != s[sz - i - 1]):
            ok = False
    if(ok):
        return "YES the string is palindrome"
    else:
        return "NO the string is not palindrome"

def main():
    s = str(input("String: "))
    check1 = palindromeCheckV1(s)
    check2 = palindromeCheckV2(s)
    print(f"check 1: {check1}")
    print(f"check 2: {check2}")

if(__name__ == "__main__"):
    main()