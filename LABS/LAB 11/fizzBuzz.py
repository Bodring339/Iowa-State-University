# Muhammad Muhamedjonov
# LAB 11 (K), 11-10-2025
# fizz Buzz game

def fizzBuzzModulus(n):
    res = []
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if i % 7 == 0:
            s += "Bazz"
        if s == "":
            s = str(i)

        res.append(s)

    return res

def fizzBuzzDict(n):
    res = []
    deff = {
        3: "Fizz",
        5: "Buzz",
        7: "Bazz"
    }

    for i in range(1, n + 1):
        s = ""
        for x, y in deff.items():
            if i % x == 0:
                s += y

        if s == "":
            s = str(i)
        res.append(s)

    return res
def main():
    n = int(input("Enter an integer: "))
    
    mod = fizzBuzzModulus(n)
    print(f"Modulus: {mod}")

    dikt = fizzBuzzDict(n)
    print(f"Dictionary: {dikt}")

if __name__ == "__main__":
    main()