"""
Muhammad Muhamedjonov, 10.28.2025, 
LAB 7, Determine if the list is palindromic
"""

def makel():
    a = []
    while(True):
        s = str(input())
        if(s == "*"):
            break
        a.append(s)
    return a

def palindromeList(a):
    ok = 1
    n = len(a)
    for i in range(int(n / 2)):
        if(a[i] != a[n - i - 1]):
            ok = 0
    if(ok == 1):
        return True
    else:
        return False

def main():
    a = makel()
    ans = palindromeList(a)
    print(ans)

if(__name__ == "__main__"):
    main()