"""
Muhammad Muhamedjonov, 10.15.2025, 
LAB 6, Finding index of first substring in python
"""

def findSubStringV1(s, t):
    ind = s.find(t)
    return ind

def findSubStringV2(s, t):
    ind = -1
    if(t in s):
        ind = s.index(t)
    return ind

def findSubstringV3(s, t):
    f = -1
    for i in range (len(s) - len(t) + 1):
        ok = True
        for j in range (len(t)):
            if(t[j] != s[i + j]):
                ok = False
        if(ok == True):
            f = i
            break
    return f

def main():
    s = str(input("String: "))
    t = str(input("Substring: "))
    ind1 = findSubStringV1(s, t)
    ind2 = findSubStringV2(s, t)
    ind3 = findSubStringV2(s, t)
    print(ind1, ind2, ind3)
    # if(ind1 != -1):
    #     print(f"The substring '{t}' was found by findSubStringV1() at index {ind1}.")
    # else:
    #     print(f"{ind1}. The substring '{t}' was not found by findSubStringV1() in the string.")
    # if(ind2 != -1):
    #     print(f"The substring '{t}' was found by findSubStringV2() at index {ind2}.")
    # else:
    #     print(f"{ind2}. The substring '{t}' was not found by findSubStringV1() in the string.")
    # if(ind3 != -1):
    #     print(f"The substring '{t}' was found by findSubStringV2() at index {ind3}.")
    # else:
    #     print(f"{ind3}. The substring '{t}' was not found by findSubStringV1() in the string.")

if(__name__ == "__main__"):
    main()
