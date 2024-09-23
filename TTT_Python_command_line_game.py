import time
import random
# Holds all board values
Board = {1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " "}

#keeps track of number of moves
count = 0



# Printing the board function with values
def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def display_coordinates():
    print("Here is an example board with coordinates within their corresponding spaces\n")
    print("1 | 2 | 3")
    print("--|---|--")
    print("4 | 5 | 6")
    print("--|---|--")
    print("7 | 8 | 9 \n")
    print('\nCreating Empty Board...\n')
    time.sleep(1)

class Token:
    def __init__(self, symbol):
        self.symbol = symbol

    def move(self):
        global count
        printBoard(Board)
        move = input(f"It is {self.symbol} turn. Move to which place (1-9): ")
        if move.isdigit(): # Method checks if input is valid 
            move = int(move)
            if move in Board and Board[move] == " ":
                count += 1
                Board[move] = self.symbol
                return True
            elif move not in Board:
                print("Invalid move. Please pick a number between 1 and 9.")
                if self.symbol == "X":
                    x_token.move()
                else:
                    o_token.move()
            else:
                print("Place is already taken. Please pick an empty space.")
                if self.symbol == "X":
                    x_token.move()
                else:
                    o_token.move()
        else:
            print("Please enter a valid number.")
            if self.symbol == "X":
                    x_token.move()
            else:
                o_token.move()
        return False
    
    def cpu_move(self, Board):
        global count
        empty_positions = [position for position, value in Board.items() if value == " "] #chooses a random empty space on the board
        if empty_positions :
            move = random.choice(empty_positions)
            count += 1
            Board[move] = self.symbol
            return True
        else:
            return False
        
        

x_token = Token("X")
o_token = Token("O")
cpu_token = Token("O")

# Checking for a win
def checkBoard():
    global count  # accessing var

    # All the following if and elif statements check for a winning move
    if Board[7] == Board[8] == Board[9] == "X":
        repeatFuncX()
    elif Board[4] == Board[5] == Board[6] == "X":
        repeatFuncX()
    elif Board[1] == Board[2] == Board[3] == "X":
        repeatFuncX()
    elif Board[1] == Board[4] == Board[7] == "X":
        repeatFuncX()
    elif Board[2] == Board[5] == Board[8] == "X":
        repeatFuncX()
    elif Board[3] == Board[6] == Board[9] == "X":
        repeatFuncX()
    elif Board[1] == Board[5] == Board[9] == "X":
        repeatFuncX()
    elif Board[3] == Board[5] == Board[7] == "X":
        repeatFuncX()
    elif Board[7] == Board[8] == Board[9] == "O":
        repeatFuncO()
    elif Board[4] == Board[5] == Board[6] == "O":
        repeatFuncO()
    elif Board[1] == Board[2] == Board[3] == "O":
        repeatFuncO()
    elif Board[1] == Board[4] == Board[7] == "O":
        repeatFuncO()
    elif Board[2] == Board[5] == Board[8] == "O":
        repeatFuncO()
    elif Board[3] == Board[6] == Board[9] == "O":
        repeatFuncO()
    elif Board[1] == Board[5] == Board[9] == "O":
        repeatFuncO()
    elif Board[3] == Board[5] == Board[7] == "O":
        repeatFuncO()

    # When count is 9 means a draw cause the board is filled
    if count == 9:
        printBoard(Board)
        clearBoard()
        print("Draw!!")
        replay()
        count = 0


# Simplifies code instead of repetition
def repeatFuncX():
    printBoard(Board)
    printWinnerX()


# Simplifies code instead of repetition
def repeatFuncO():
    printBoard(Board)
    printWinnerO()


# Printing win statements for X
def printWinnerX():
    print("Player X won!")
    print("End Game")
    replay()


# Printing win statements for O
def printWinnerO():
    print("Player O won!")
    print("End Game")
    replay()


# Clearing the board
def clearBoard():
    global count  # Accessing count
    count = 0  # Set count to 0 to restart

    # while loop to simplify code
    i = 1
    while i < 10:  # While i is less than 10
        Board[i] = " "  # Set the value of i of board to " " which means emtpy
        i += 1 
    # Repeats 9 times


# Replaying game
def replay():
    replayStr = str(input("Would you like to replay the game? (y/n): "))  # Getting input as a string
    if replayStr == "y" or replayStr == "Y":  # If input is Y or y
        clearBoard()
        x_token.move()
    elif replayStr == "n" or replayStr == "N":  # If input is N or n
        main_menu()
    else:
        # If input is not Y or N
        print("Invalid input, Try again!")
        replay()

def Single_game():
    print("\nYou chose Single player\n")
    display_coordinates()
    global count
    while True:
        # For start
        if x_token.move():
            checkBoard()
        print("It is now Computer's turn")
        cpu_token.cpu_move(Board)
        checkBoard()
        if count == 0:
            x_token.move()

        # Checking for a draw
        if count == 9:
            clearBoard()
            print("Draw!!")
            replay()
            count = 0

def Two_Player():
    # Continuous loop
    print("\nYou chose Two player\n")
    display_coordinates()
    global count
    while True:
        # For start
        if x_token.move():
            checkBoard()
        o_token.move()
        checkBoard()
        if count == 0:
            x_token.move()

        # Checking for a draw
        if count == 9:
            clearBoard()
            print("Draw!!")
            replay()
            count = 0
    

def main_menu():
    print("Tic-Tac-Toe Command Line Game")
    print("------------------------------")
    print("1. Start Single Player")
    print("2. Start Two Player")
    print("3. Exit Program")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Start Single player
        Single_game()
    elif choice == "2":
        # Start Two player
        Two_Player()
    elif choice == "3":
        # Quit the game
        print("Goodbye!")
        exit()
    else:
        print("\nINVALID CHOICE. PLEASE TRY AGAIN.\n")
        main_menu()
    # Recursive call to display the menu again
    # main_menu()

# Start the program by calling the main_menu function
if __name__ == "__main__":
    main_menu()
