"""Sliding Tile Puzzle, by Al Sweigart al@inventwithpython.com
Slide the numbered tiles into the correct order.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, puzzle"""

''' Could you this to increase recursion depth: sys.setrecursionlimit'''
import random, sys
sys.setrecursionlimit(3000)
BLANK = '  '  # Note: This string is two spaces, not one.


def main():
    print('''Sliding Tile Puzzle, by Al Sweigart al@inventwithpython.com

    Use the WASD keys to move the tiles
    back into their original order:
           1  2  3  4  5
           6  7  8  9  10
           11 12 13 14 15
           16 17 18 19 20
           21 22 23 24   ''')
    input('Press Enter to begin...')

    gameBoard = getNewPuzzle()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('You won!')
            sys.exit()


def getNewBoard():
    """Return a list of lists that represents a new tile puzzle."""
    return [['1 ', '6 ', '11', '16', '21'], ['2 ', '7 ', '12', '17', '22'],
            ['3 ', '8 ', '13', '18', '23'], ['4 ', '9 ', '14', '19', '24'], ['5 ', '10', '15', '20', BLANK]]


def displayBoard(board):
    """Display the given board on the screen."""
    labels = [board[0][0], board[1][0], board[2][0], board[3][0], board[4][0],
              board[0][1], board[1][1], board[2][1], board[3][1], board[4][1],
              board[0][2], board[1][2], board[2][2], board[3][2], board[4][2],
              board[0][3], board[1][3], board[2][3], board[3][3], board[4][3],
              board[0][4], board[1][4], board[2][4], board[3][4], board[4][4]]
    boardToDraw = """
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+

""".format(*labels)
    print(boardToDraw)


def findBlankSpace(board):
    """Return an (x, y) tuple of the blank space's location."""
    for x in range(5):
        for y in range(5):
            if board[x][y] == '  ':
                return (x, y)


def askForPlayerMove(board):
    """Let the player select a tile to slide."""
    blankx, blanky = findBlankSpace(board)

    w = 'W' if blanky != 4 else ' '
    a = 'A' if blankx != 4 else ' '
    s = 'S' if blanky != 0 else ' '
    d = 'D' if blankx != 0 else ' '
    x = 'X'

    while True:
        print('                          ({})'.format(w))
        print('Enter WASD (or QUIT): ({}) ({}) ({})         ({})'.format(a, s, d, x))

        response = input('> ').upper()
        if response == 'QUIT':
            sys.exit()
        if response in (w + a + s + d + x).replace(' ', ''):
            return response


def makeMove(board, move):
    """Carry out the given move on the given board."""
    # Note: This function assumes that the move is valid.
    bx, by = findBlankSpace(board)

    if move == 'W':
        board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]
    elif move == 'A':
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif move == 'S':
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
    elif move == 'D':
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]
    elif move == 'X':
        auto_play(board)


def makeRandomMove(board):
    """Perform a slide in a random direction."""
    blankx, blanky = findBlankSpace(board)
    validMoves = []
    if blanky != 4:
        validMoves.append('W')
    if blankx != 4:
        validMoves.append('A')
    if blanky != 0:
        validMoves.append('S')
    if blankx != 0:
        validMoves.append('D')

    makeMove(board, random.choice(validMoves))


def auto_play(curr_board):
    curr_state = [row[:] for row in curr_board]
    for i in range(40):
        makeRandomMove(curr_state)

        if curr_state == getNewBoard():
            print('The algorithm won!')
            sys.exit()

    print("Final Unsuccessful State")
    displayBoard(curr_state)

    # Recursion in case of failed attempt
    auto_play(curr_board)





def getNewPuzzle(moves=16):
    """Get a new puzzle by making random slides from a solved state."""
    board = getNewBoard()

    for i in range(moves):
        makeRandomMove(board)
    return board


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()