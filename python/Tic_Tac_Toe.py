import random

l1 = [" "," "," "]
l2 = [" "," "," "]
l3 = [" "," "," "]

def printboard():
    print(l1)
    print(l2)
    print(l3)

def userinput():
    global l1
    global l2
    global l3

    board = [l1,l2,l3]

    while True:

        row = int(input("Enter your row (1-3): ")) - 1
        coulmn = int(input("Enter your column (1-3): ")) - 1

        if row not in [0,1,2] or coulmn not in [0,1,2]:
            print("Invalid Choice")
            continue

        if board[row][coulmn] == " ":
            board[row][coulmn] = "X"
            break

        else:
            print("Already Exists Try Again")

def computerinput():
    global l1
    global l2
    global l3

    board = [l1,l2,l3]

    while True:

        row = random.randint(0,2)
        coulmn = random.randint(0,2)

        # simple blocking move
        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == " ":
            board[0][2] = "O"
            break

        elif board[row][coulmn] == " ":
            board[row][coulmn] = "O"
            break

def scoring():

    board = [l1,l2,l3]

    if (
        board[0][0] == board[0][1] == board[0][2] == "X" or
        board[1][0] == board[1][1] == board[1][2] == "X" or
        board[2][0] == board[2][1] == board[2][2] == "X" or

        board[0][0] == board[1][0] == board[2][0] == "X" or
        board[0][1] == board[1][1] == board[2][1] == "X" or
        board[0][2] == board[1][2] == board[2][2] == "X" or

        board[0][0] == board[1][1] == board[2][2] == "X" or
        board[0][2] == board[1][1] == board[2][0] == "X"
    ):
        printboard()
        print("Player Wins")
        return "win"

    elif (
        board[0][0] == board[0][1] == board[0][2] == "O" or
        board[1][0] == board[1][1] == board[1][2] == "O" or
        board[2][0] == board[2][1] == board[2][2] == "O" or

        board[0][0] == board[1][0] == board[2][0] == "O" or
        board[0][1] == board[1][1] == board[2][1] == "O" or
        board[0][2] == board[1][2] == board[2][2] == "O" or

        board[0][0] == board[1][1] == board[2][2] == "O" or
        board[0][2] == board[1][1] == board[2][0] == "O"
    ):
        printboard()
        print("Computer Wins")
        return "win"

    elif " " not in l1 and " " not in l2 and " " not in l3:
        printboard()
        print("Its a Tie")
        return "win"

    return "continue"

while True:

    l1 = [" "," "," "]
    l2 = [" "," "," "]
    l3 = [" "," "," "]

    print("************************ WELCOME TO TIC TAC TOE ************************")

    game_running = True

    while game_running:

        printboard()

        userinput()

        result = scoring()

        if result == "win":
            break

        computerinput()

        result = scoring()

        if result == "win":
            break

    retry = int(input("Do you want to play again? 1 = Yes, 0 = No: "))

    if retry == 1:
        continue

    elif retry == 0:
        print("Thanks for playing")
        break

    else:
        print("Invalid Input")
        break
