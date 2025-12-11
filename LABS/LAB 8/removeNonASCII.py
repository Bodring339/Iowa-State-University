"""
Muhammad Muhamedjonov, 11-05-2025
LAB 8, This code creates a new text file from the given text file with removing non-ASCII characters
"""

def read_file(filename):
    orig = ""
    with open(filename, "r", encoding="utf-8") as f:
        orig = f.read()
    return orig


def removeNonASCII(text):
    cleaned = ""
    for c in text:
        if ord(c) < 128:
            cleaned += c
    return cleaned


def make(filename, cleaned):

    new_filename = filename[0:len(filename) - 4] + "_clean.txt"

    with open(new_filename, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print(f"Clean file written as: {new_filename}")


def main():
    filename = input("Enter the filename (with .txt): ")

    orig = read_file(filename)

    cleaned = removeNonASCII(orig)

    make(filename, cleaned)


if (__name__ == "__main__"):
    main()
