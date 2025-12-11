"""
Muhammad Muhamedjonov, 10.15.2025, 
LAB 6, Reversing string in python
"""

def reverseStringV1(s):
    rs = s[::-1]
    return rs

def reverseStringV2(s):
    rs = "".join(reversed(s))
    return rs

def reverseStringV3(s):
    sz = len(s)
    rs = ""
    for i in range(0, sz):
        rs += s[sz - i - 1]
    return rs

def reverseStringV4(s):
    rs = ""
    for i in s:
        rs = i + rs
    return rs

def reverseStringV5(s):
    sz = len(s)
    rs = ""
    while(sz > 0):
        rs = rs + s[sz - 1]
        sz -= 1
    return rs

def main():
    s = str(input("String: "))
    rs1 = reverseStringV1(s)
    rs2 = reverseStringV2(s)
    rs3 = reverseStringV3(s)
    rs4 = reverseStringV4(s)
    rs5 = reverseStringV5(s)
    print(f"reversed strings:\n    version 1: {rs1}\n    version 2: {rs2}\n    version 3: {rs3}\n    version 4: {rs4}\n    version 5: {rs5}")

if (__name__ == "__main__"):
    main()
