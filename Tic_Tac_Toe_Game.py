# Tic-Tac-Toe (井字游戏)
"""
Two people play Tic Tac Toe with paper and pencil.
One player is X and the other player is O.
Players take turns placing their X or O.
If a player gets three of their marks on the board in a row,
column or one of the two diagonals, they win.
When the board fills up with neither player winning,
the game ends in a draw.
"""

import random


def drawBoard(board):
    """
    This function prints out the board that it was passed.
    Board is a list of 10 strings representing the board (ignore index 0)
    The board is numbered like the keyboard's number pad.
    """
    string1 = '   |   |'
    string2 = '-----------'

    print(string1)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(string1)

    print(string2)

    # please complete the remain codes

    print(string1)
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(string1)

    print(string2)

    print(string1)
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(string1)


def inputPlayerLetter():
    """
    Lets the player type which letter ('X' or 'O') they want to be.
    Returns a list with the player's letter as the first item,
    and the computer's letter as the second.

    """
    letter = ''
    # set the user's input to letter
    # if letter is neither 'X' nor 'O', ask user to input again
    # until letter is 'X' or 'O'
    # while not (letter == 'X' or letter == 'O'):
    while True:
        letter = input("Do you wangt to be X or O?")
        if letter.upper() == "X":
            return ["X", "O"]
        elif letter.upper() == "O":
            return ["O", "X"]
        else:
            print("Input error,please input again!")

    # if letter is 'X', return ['X','O']
    # else return ['O','X']


def whoGoesFirst():
    """
    randomly choose the player who goes first
    """
    # use the randint function in random module
    # then return a random integer from [0,1]
    # if the return integer is 0, return 'computer'
    # else return 'player'
    x = random.randint(0,1)
    if x == 0 :
        return "computer"
    else:
        return "player"


def  playAgain():
    """This function returns True if the player wants to play again,
    otherwise it returns False"""
    print('Do you want to play again?(yes or no)')

    # write one line code to implement this function
    return input().lower() == "yes"


# This function is complete
def makeMove(board,letter,move):
    """This function adds the player's move to the board"""
    board[move] = letter    #!!!


def isWinner(board, letter):
    """
    Given a board and a player's letter,
    this function returns True if the player has won.
    """
    for i in range(1, 10, 3):
        if board[i] == board[i + 1] == board[i + 2] == letter:
            return True
    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 6] == letter:
            return True
    if board[1] == board[5] == board[9] == letter or board[3] == board[5] == board[7] == letter:
        return True

    return False


def isSpaceFree(board,move):
    """Return True if the passed move is free on the passed board"""
    # write one line of code to finish this function
    return board[move] ==" "   #是空格返回true


def getPlayerMove(board):
    """Let the player type in their move."""
    # ask the player to input their move
    # until move is a number between 1 to 9 and the move is free on board
    # then return move as a number
    while True:
        pmove = int(input("Please input your move:"))
        if pmove <= 9 and pmove >= 1 and isSpaceFree(board, pmove) == True:
            return pmove
        else:
            print("Input is error or space is not free!Please input again!")


def chooseRandomMoveFromList(board, movesList):
    """
    Returns a valid move from the passed list on the passed baord.
    Returns None if there is no valid move"""
    possibleMoves = []
    # for each move in movesList,
    # if the move is free on board,
    # then add the move to possibleMoves
    for item in movesList:
        if isSpaceFree(board, item) == True:
            possibleMoves.append(item)
    # if the length of possibleMoves is not 0, then randomly choose one and return it
    # else renturn None
    if len(possibleMoves) != 0:
        return possibleMoves[random.randint(0,len(possibleMoves)-1)]
    else:
        return None


def getComputerMove(board, computerLetter):
    """
    Given a board and the computer's letter,
    determine where to move and return that move
    """
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # Here is our algorithm for our Tic Tac Toe AI:
    # first, check if we can win in the next move
    for i in range(1, 10):
        copy = board.copy()
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = board.copy()
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5
    # Move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    """
    Return True if every space on the board has been taken.
    Otherwise return False.
    """
    for i in range(1, 10):
        if board[i] == " ":
            return False
    return True


# the main body of the Tic Tac Toe
print('Welcome to Tic Tac Toe!')
while True:
    theBoard = [" "] * 10  # reset the board, finish this line of code
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':  # player's turn
            # use your function to print out the board
            drawBoard(theBoard)
            # use your function to get player's move, and set it to variable move
            playerMove = getPlayerMove(theBoard)
            # adds the player's move to the board
            makeMove(theBoard, playerLetter, playerMove)
            if isWinner(theBoard, playerLetter):  # if the player has won
                # print out the board
                drawBoard(theBoard)
                # print the prompt message "Hooray! You have won the game!"
                print("Hooray! You have won the game!")
                # set gameIsPlaying to False
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):  # if the board is full
                    # print out the board
                    drawBoard(theBoard)
                    # print the prompt message "The game is a tie!"
                    print("The game is a tie!")
                    # end the loop
                    break
                else:
                    # set turn to computer
                    turn = "computer"

        else:
            # computer's turn
            move = getComputerMove(theBoard, computerLetter)

            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):  # if the computer has won
                # print out the board
                drawBoard(theBoard)
                # print the prompt message "The computer has beaten you! You lose."
                print("The computer has beaten you! You lose.")
                # set gameIsPlaying to False
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):  # if the board is full
                    # print out the board
                    drawBoard(theBoard)
                    # print the prompt message "The game is a tie!"
                    print("The game is a tie!")
                    # end the loop
                    break
                else:
                    # set turn to player.
                    turn = "player"


    if not playAgain():
        break