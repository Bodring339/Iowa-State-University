# Muhammad Muhamedjonov, 12-05-2025
# Assignment 6, COM S 1270 - 02 (LAB K)
#
# This is a simple python code version of the classic board game called "Candy Land" - here called "Candy Realm".

import random
import time

COLORS = ["R", "G", "B", "Y", "O", "P"] # Red, Green, Blue, Yellow, Orange, Purple
BOARD_SIZE = 30
COPIES_CARD = 5
GOAL = "GOAL"

def get_valid_num(minv, maxv):
    while (True):
        num = input(f"How many people will play ({minv}-{maxv})? ", )
        try:
            val = int(num)
            if (minv <= val <= maxv):
                return val
            else:
                print(f"Invalid input. Please enter a positive integer from {minv} to {maxv}")
        except ValueError:
            print(f"Invalid input: Please enter a positive integer from {minv} to {maxv}.")

def create_deck():
    deck = COLORS * COPIES_CARD
    random.shuffle(deck)
    return deck

def generate_board():
    board = []
    for i in range(BOARD_SIZE):
        board.append(random.choice(COLORS))
    board.append(GOAL)
    return board

def find_next_pos(board, current_pos, color):
    next = len(board) - 1
    for i in range(current_pos + 1, len(board)):
        if (board[i] == color):
            next = i
            break
    return next

def show_game(board, players):
    print("\nBOARD: ")
    stri = "START"
    ad = ""
    for p in players:
        if (p['pos'] == -1):
            if (len(ad)):
                ad += ", "
            ad += str(p['id'])
    stri += "-[" + ad + "]"

    for i in range(len(board)):
        stri += " " + board[i]
        ad = ""
        for p in players:
            if (p['pos'] == i):
                if (len(ad)):
                    ad += ", "
                ad += str(p['id'])
        if (len(ad) > 0):
            stri += "-[" + ad + "]"

    print(stri)
    print("=" * 50 + "\n")

def play_game():
    print("\n    YOU STARTED A NEW GAME    ")
    
    num_humans = get_valid_num(1, 4)
    
    players = []
    for i in range(4):
        is_human = i < num_humans
        players.append({
            "name": f"Player {i + 1} (Human)" if (is_human) else f"Player {i + 1} (Bot)",
            "id": i + 1,
            "pos": -1,
            "is_human": is_human
        })

    board = generate_board()
    deck = create_deck()
    game_over = False
    turn = 0

    while (game_over == False):
        cplayer = players[turn]

        if (len(deck) == 0):
            deck = create_deck()

        print(f"\nTurn: {cplayer['name']}")
        
        if (cplayer['is_human']):
            show_game(board, players)
            do = input("Press [ENTER] to pick a card, or [q] to quit: ").strip()
            do = do.lower()
            while (do != '' and do != 'q'):
                print("Invalid input")
                do = input("Press [ENTER] to pick a card, or [q] to quit: ").strip()
                do = do.lower()
            if (do == 'q'):
                print("Quitting the game...")
                return
        else:
            time.sleep(1.5) 

        card = deck.pop()
        print(f"---> You got: [{card}]")

        new_pos = find_next_pos(board, cplayer['pos'], card)
        dist = new_pos - cplayer['pos']
        cplayer['pos'] = new_pos
        
        if (board[new_pos] == GOAL):
            destination = "FINISH"
        else:
            destination = f"{new_pos+1} ({board[new_pos]})"
            
        print(f"---> {cplayer['name']} goes {dist} space(s) forward to space {destination}.")

        if (board[new_pos] == GOAL):
            show_game(board, players)
            print(f"\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print(f" CONGRATULATIONS! {cplayer['name']} WON THE GAME!")
            print(f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
            game_over = True
        
        turn = (turn + 1) % 4
        print()

def print_instructions():
    print("\n    INSTRUCTIONS    ")
    print("1. There are four players in one game - Humans and Bots(AI))")
    print("2. Each player in his turn picks a card from the top of deck.")
    print("3. Player moves to the next nearest space of his card's color.")
    print("4. The first player achieving GOAL space wins.\n")

def main():
    print("\nCandy Realm!\n")
    print("By: Muhammad Muhamedjonov")
    print("[COM S 127 02 (K)]\n")

    while (True):
        print("MAIN MENU:")
        print("[p]lay game")
        print("[i]nstructions")
        print("[q]uit")
        
        choice = input().strip()
        choice = choice.lower()

        if (choice == 'p'):
            play_game()
            print()
        elif (choice == 'i'):
            print_instructions()
        elif (choice == 'q'):
            print("You left the game. GoodBye!\n")
            break
        else:
            print("Invalid input. Try again\n")

if (__name__ == "__main__"):
    main()