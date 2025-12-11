# Muhammad Muhamedjonov, 11-04-2025
# Assignment 1, COM S 1270 - 02 (LAB K)
#
# This is the code which writes 4 zany texts

def zanyText1():
    res = ""
    verb1 = str(input("Verb: "))
    verb2 = str(input("Verb: "))
    noun = str(input("Noun: "))
    pnoun = str(input("Plural noun: "))
    res = "To " + verb1 + " or not to " + verb1 + ", that is the question.\nWhether 'tis nobler in the mind to " + verb2 + "\nThe slings and arrows of outrageous fortune,\nOr to take arms against a " + noun + " of " + pnoun + "\nAnd by opposing end them."
    return res

def zanyText2():
    res = ""
    character = str(input("Character: "))
    place = str(input("Place: "))
    fperson = str(input("Famous person: "))
    noun = str(input("Noun: "))
    verb = str(input("Verb: "))
    pverb = str(input("Past tense verb: "))
    res = "When " + character + " came to the " + place + ", he saw a " + fperson + "'s " + noun + ", but " + fperson + " wasn't there. Then he decided to " + verb + " it and " + pverb + " it with his friend"
    return res

def zanyText3():
    actor = str(input("Actor: "))
    place = str(input("Place: "))
    country = str(input("Country: "))
    adjective = str(input("Adjective: "))
    res = f"This summer I and my friend {actor} visited {place} which is in center of {country}. It was amazing, and suddenly I woke up and realized that it was just a {adjective} dream. I was crying so hard."
    return res

def zanyText4():

    number = int(input("Number: "))
    vegetable = str(input("Vegetable: "))
    fruit = str(input("Fruit: "))
    meat = str(input("Meat: "))
    sauce = str(input("Sauce: "))
    adverb = str(input("Adverb: "))
    adjective = str(input("Adjective: "))
    res = f"Here is my grandfather's signature salad's ingredients: \nFirst, cut {number} {vegetable} into small cubes. Then grind one {fruit} on top of it. Put grilled {meat} as much as you want. Then season with {sauce} and soy sauce. Mix everything very {adverb} and enjoy my grandfather's, {adjective} signature salad!"
    return res

def main():

    print("Zany Text!")
    print()

    print("By: Muhammad Muhamedjonov")
    print("[COM S 127 02]")
    print()

    print("ZanyText #1\n")
    print(zanyText1())
    print()

    print("ZanyText #2\n")
    print(zanyText2())
    print()

    print("ZanyText #3\n")
    print(zanyText3())
    print()
    
    print("ZanyText #4\n")
    print(zanyText4())
    print();


if(__name__ == "__main__"):
    main()