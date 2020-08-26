'''
Name: Ali Raza Zaidi
Project: Tic Tac Toe - Complete 2020 Python Bootcamp Milestone Project 1
Description: Two-player Tic Tac Toe game
Github Repository: https://github.com/AliRZ-02/TicTacToe
Creation Date: 08/25/2020
Last Modified: 08/26/2020
'''
from random import shuffle

'''Global Variables to be declared for the script'''
user_selection=0
restart = 'p'
game_over = False
winCount = False

def start_of_game ():
    '''
    This function is called at the beginning of every new game - it sets the board and takes the players' names
    and returns them.
    '''
    print("Are you ready to play Tic Tac Toe?")
    playerNames = []
    for i in range (0,2):
        playerNames.append(input("Please enter the name of player {}: ".format(i + 1)))
    current_board = set_board()
    return playerNames,current_board

def set_board ():
    '''
    This function sets the board to its default values and prints a version out for the user. It also returns
    the rows.
    '''
    rows = [['1','2','3'],['4','5','6'],['7','8','9']]
    for i in range (0,3):
        print(rows[i])
    return rows

def play_game(game_over,current_board):
    '''
    This function is the main game function in the script as it shuffles the player order and allows for player
    turns and checks
    '''
    shuffle(playerNames)
    while not game_over:
        for i in range(0, 2):
            current_board = get_user_selection(playerNames, current_board, playerNames[i],i)
            game_over,tieCount = check_game(current_board,i)
            if game_over == True:
                if tieCount !=3:
                    print("")
                    print("You win {}!".format(playerNames[i]))
                break

def get_user_selection (playerNames,current_board,current_player,i):
    '''
    This function accepts and validated the user response and sends it to another function to be updated
    '''
    while True:
        try:
            user_selection = input("{}, Which position would you like to select: ".format(playerNames[i].strip()))
            if int(user_selection) in range(1,10) and ((user_selection in current_board[0]) or
                                                       (user_selection in current_board[1]) or
                                                       (user_selection in current_board[2])):
                break
            else:
                print("Invalid Response")
        except ValueError:
            print("Invalid Response")
    current_board = update_board(user_selection,current_board,current_player)
    return current_board

def update_board (user_selection,current_board,current_player):
    '''
    This function takes the user selection and changes the board accordingly
    '''
    print("Thank you for your selection. The board has been updated as follows")
    if playerNames[0] == current_player:
        letter = 'X'
    else:
        letter = "O"
    if user_selection in current_board[0]:
        current_board[0][int(user_selection)-1] = letter
    elif user_selection in current_board[1]:
        current_board[1][int(user_selection)-4] = letter
    else:
        current_board[2][int(user_selection)-7] = letter
    for i in range(0, 3):
        print(current_board[i])
    return current_board

def check_game (current_board,i):
    '''
    This function takes the current board and checks to see if the game has been won or if it is tied, and returns said
    values
    '''
    tieCount = 0
    for j, row in enumerate(current_board):
        if len(set(row)) == 1:
            return True,tieCount
        elif current_board[0][j] == current_board[1][j] and current_board[i][j] == current_board[2][j]:
            return True,tieCount
        elif j == 0 and (current_board[0][j] == current_board[1][j+1] and current_board[0][j] == current_board[2][j+2]):
            return True,tieCount
        elif j == 0 and (current_board[2][j] == current_board[1][j+1] and current_board[0][j+2] == current_board[2][j]):
            return True,tieCount
        elif 'X' in row and 'O' in row and (len(set(row)) == 2 or len(set(row)) == 1):
            tieCount = tieCount + 1
    if tieCount == 3:
        print("")
        print("It's a tie!")
        return True,tieCount
    tieCount = 0
    return False,tieCount

#Start of Main Code
playerNames,current_board = start_of_game()

while restart == 'p':
    play_game(game_over,current_board)
    restart = input("Press 'P' to play again or any other key to quit: ")
    if restart.lower() == 'p':
        current_board = set_board()
        game_over = False
    else:
        break