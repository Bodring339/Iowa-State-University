"""
Muhammad Muhamedjonov, 01.10.2025, 
LAB 4, code of how to define if the year is leap or not in python using functions
"""

def main():
    print("You were just born, Welcome to life!\n")
    print("You find yourself in a maternity hospital in the body of a newborn baby, choose you gender: 1-[male], 2-[female]")
    t = int(input())
    if(t == 2):
        print("Congratulations! You were born the most ordinary and healthy baby! You start to cry a little, your mother is very happy about your birth, and you begin your life as the most ordinary child! Good luck in life!")
    else:
        print("You decide your own destiny! Make your choice wisely and correctly!")
        print("Your next steps are: 1-[start speaking in the voice of a grown man], 2-[make a sigme face], 3-[start crying], 4-[just be quiet]")
        t = int(input())
        if(t == 1):
            print("You decide to start speaking in the voice of a grown man. Your mother faints from shock. All the doctors are in shock. The head doctor asks you: who are you and what do you need?")
            print("What to you do next?: 1-[pretend that nothing happened and that it was all just their imagination], 2-[say that you are an alien], 3-[get up on your feet and run away]")
        elif(t == 2):
            print("Everyone starts filming you on their phones and posting them on social media. You become the most popular baby in history.")
            print("What do you do next? 1-[start making tik-tok videos and become a tik-toker], 2-[become an actor and star in American films], 3-[You accidentally made such a face. You continue to live like an ordinary child.]")
        elif(t == 3):
            print("Everyone starts to calm you down")
            print("What do you do next? 1-[You start crying even louder and harder. You start screaming at the top of your lungs. No one likes it. Your dad starts regretting that you were born.], 2-[you just calm down and start feeling very sleepy], 3-[You get wings and fly out of the window]")
        elif(t == 4):
            print("Everyone starts to like you, your parents are crazy with happiness, all the doctors calm down.")
            print("What do you do next? 1-[just lie with your eyes open]")
        print("You suddenly feel sleepy, and within a few seconds you're already falling asleep. When you wake up, you realize it was a dream and you're actually already an adult.")



if __name__ == "__main__":
    main()
