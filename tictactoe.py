# Two user tic tac toe game
# player1 is 'X', player2 is 'O'

def displayBoard(board) : 
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-' + ' + ' + '-' + ' + ' + '-')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-' + ' + ' + '-' + ' + ' + '-')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def isValidMove(board, index) :
    # Checking if out of bounds
    if index<1 or index>9:
        return False

    # making it 0-indexed
    index -= 1

    # if valid
    if(board[index] == ' '):
        return True
    return False

def makeMove(board, index, mark) :
    board[index-1] = mark

def checkWinner(board, mark) :
    # check row
    for i in range(0, len(board), 3) :
        if(board[i] == mark and board[i+1] == mark and board[i+2] == mark) :
            return True

    # check col
    for i in range(0, len(board), 3) :
        j = i//3
        if(board[j] == mark and board[j+3] == mark and board[j+6] == mark) :
            return True

    # check diagonal
    return ((board[0] == mark and board[4] == mark and board[8] == mark) or
   (board[2] == mark and board[4] == mark and board[6] == mark))


# Playing the game
print('\nWelcome to TicTacToe!')

player1 = input("\nEnter first player's name?\n")
player2 = input("\nEnter second player's name?\n")

print("\nHello " + player1 + ' and ' + player2 + '!')

board = [' '] * 9
users = [player1, player2]
marker = ['X', 'O']
userIndex = 0
count = 1
winner = False

while count <= 9 and winner == False:
    print('\n')
    displayBoard(board)
    gameIndex = 0

    while isValidMove(board, gameIndex) == False:
        gameIndex = int(input("\nIt's your turn " + users[userIndex] + ". Select an index to place your move:\n"))

    makeMove(board, gameIndex, marker[userIndex])

    if checkWinner(board, marker[userIndex]) == True :
        winner = True
        print('\n')
        displayBoard(board)
        print('\nGame Over!')
        print('\n' + users[userIndex] + ' Won!!!')

    userIndex = 1 - userIndex
    count += 1

if count == 10 and winner == False:
    print('\n')
    displayBoard(board)
    print('\nGame Over!')
    print("\nIt's a Tie!!!\n")

