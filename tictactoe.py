def get_player1_choice():
    choice = "wrong"
    while choice not in ["X","O"]:
        choice = input("Player 1, do you want to be X or O: ").upper()
        if choice not in ["X","O"]:
            choice = input("Invalid choice! Enter X or O: ").upper()
    return choice

def is_player_ready():
    choice = "wrong"
    while choice not in ["Yes","No"]:
        choice = input("Player 1, are you ready? Enter Yes or No: ")
        if choice not in ["Yes","No"]:
            choice = input("Invalid choice! Enter Yes or No: ")
    if choice == "Yes":
        return True
    return False

def update_board(symbol, players, board, position):
    board[position] = symbol

#can def make this function more simple. just print everything manually
def print_current_board(board):
    blank_row = "   |   |   "
    for i, element in enumerate(board): #will iterate 9 times
        if i != 0:
            if i==1:
                print(blank_row)
                print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
                
            if i==4 or i==7:
                print(blank_row)
                print("------------")
                print(blank_row)
                print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
            if i==9:
                print(blank_row)

def get_next_position():
    pos = 0
    while pos not in range(1,10):
        pos = int(input("Enter your next position (1-9): "))
        if pos not in range(1,10):
            pos = int(input("Invalid choice! Enter a number 1-9:  "))
    return pos

def game_won_check(board, symbol):
    print(f"current board, checking for win: {board}")

    winning_combos = ("123","456","789","147","258","369","159","357")
    for combo in winning_combos:
        if board[int(combo[0])]== symbol and board[int(combo[1])]==symbol and board[int(combo[2])]==symbol:
            print_current_board(board)
            print(f"{symbol} wins! Game over")
            return True
    return False

def replay_prompt():
    choice = "wrong"
    while choice not in ["Yes","No"]:
        choice = input("Would you like to replay? Enter Yes or No: ")
        if choice not in ["Yes","No"]:
            choice = input("Invalid choice! Enter Yes or No: ")
    if choice == "Yes":
        return True
    return False



#MAIN
replay = True
while replay:

    print("Welcome to Tic Tac Toe!")

    #FIX: make one statement
    if get_player1_choice() == "X":
        players = ("X","O")
    else:
        players = ("O", "X")

    if is_player_ready():

        turn = 1
        board = ["#"," ", " ", " ", " ", " ", " ", " ", " ", " "]
        position = "wrong"
        symbol = players[0]

        while not game_won_check(board, symbol):
            #change the user
            if turn%2==0:
                symbol = players[1]
            else:
                symbol = players[0]
            
            print_current_board(board)
            position = get_next_position()
            update_board(symbol, players, board, position)
            
            turn += 1
        replay = replay_prompt()

    else:
        print("Alright. We'll end game for now")
        break

