from IPython.display import clear_output
import random
 
def displayboard(board):
     clear_output()
     print(board[0]+' | ' + board[1] + ' | ' + board[2])
     print("----------")
     print(board[3]+' | ' + board[4] + ' | ' + board[5])
     print("----------")
     print(board[6]+' | ' + board[7] + ' | ' + board[8])


def assignXO():
    player1 = ''
    while not (player1 == 'X' or player1 == 'O'):
        player1 = input ("Player 1, please select X or O :")
        player1 = player1.upper()
        if ('X' == player1):
            player2 = 'O'
            print("Player 1 is "+ player1 + " and Player 2 is " +player2)
            return player1, player2
        elif('O' == player1):
            player2 = 'X'
            print("Player 1 is "+ player1 + " and Player 2 is " + player2)
            return player1, player2

def place_marker(board, marker, position):
    board[position] = marker


def blank_board():
    return [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def win_check(board, mark):
    for x in range(0,2):
        if board[0+x] == board[1+x] == board[2+x] == mark:
            print (mark + 'row is the WINNER')
            break
        elif board[x] == board[x+3] == board[x+3] == mark:
            print(mark + 'column is the WINNER')
            break
    if board[0] == board[4] == board[8] == mark or board[2] == board[4] == board[6] == mark:
        print (mark + ' is the diagonal WINNER')
        
def choose_first_go():
    choice = random.randint(1,100)
    if choice % 2 == 0:
        print('O goes first!')
        return 'O'
    else:
        print('X goes first!')
        return 'X'

def check_space(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

def check_full_board(board):
    used_space_count = 0
    for x in range(0,8):
        if board[x] != ' ':
            used_space_count += 1
    
    if used_space_count == 9:
        return True
    else:
        return False
    
def player_choice(board):
    while True:
        choice = int(input('Please pick a space to mark (1-9)'))
        if  choice > 9 or choice < 1:
            print(type(choice))
            print(choice)
            print('Invalid choice, please pick a number 1-9')
        else:
            if check_space(board, choice) == True:
                return(choice - 1)

def replay():
    while True:
        choice = input('Would you like to play again? (Y or N)')
        choice = choice.upper()
        if choice != 'Y' or choice != 'N':
            print('Invalid select, choose again.')
        else:
            return True



while True:
    clear_output()
    board = blank_board()
    print('Welcome to Tic Tac Toe!')
    assignXO()
    choose_first_go()
    player_choice(board)