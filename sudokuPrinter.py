import sys

def sudokuPrinter (board):
    #print (board)
    print ("-------------------------------------------------------")
    for y in range(len(board[0])):
        for x in range(len(board[1])):
            if (x == 0):
                sys.stdout.write( "|  " )
            sys.stdout.write( str(board[x][y]) )
            sys.stdout.write( "  |" )
            if (x != len(board[0]) - 1):
                sys.stdout.write( "  " )
        print ("\n-------------------------------------------------------")


def pSpaceSizePrinter (pSpace):
    print ("-------------------------------------------------------")
    size = 9
    for y in range(size):
        for x in range(size):
            if (x == 0):
                sys.stdout.write( "|  " )
            sys.stdout.write( str(len(pSpace[x][y])) )
            sys.stdout.write( "  |" )
            if (x != size - 1):
                sys.stdout.write( "  " )

        print ("\n-------------------------------------------------------")


def exampleBoard (w, h):
    board = [[0 for x in range(w)] for y in range(h)]
    board[0][0] = 1
    board[0][1] = 2
    board[0][2] = 3
    board[0][3] = 4
    return board

# Simple board:
# https://s-media-cache-ak0.pinimg.com/originals/46/a7/0e/46a70eb6a46cb44511c70c10e96bd03f.jpg
def exampleBoard2 ():
    board = [[0 for x in range(9)] for y in range(9)]

    board[0][0] = 6
    board[3][0] = 1
    board[5][0] = 8
    board[6][0] = 2
    board[8][0] = 3

    board[1][1] = 2
    board[4][1] = 4
    board[7][1] = 9

    board[0][2] = 8
    board[2][2] = 3
    board[5][2] = 5
    board[6][2] = 4

    board[0][3] = 5
    board[2][3] = 4
    board[3][3] = 6
    board[5][3] = 7
    board[8][3] = 9

    board[1][4] = 3
    board[7][4] = 5

    board[0][5] = 7
    board[3][5] = 8
    board[5][5] = 3
    board[6][5] = 1
    board[8][5] = 2

    board[2][6] = 1
    board[3][6] = 7
    board[6][6] = 9
    board[8][6] = 6

    board[1][7] = 8
    board[4][7] = 3
    board[7][7] = 2

    board[0][8] = 3
    board[2][8] = 2
    board[3][8] = 9
    board[5][8] = 4
    board[8][8] = 5

    return board


def exampleBoard2Solution ():
    board = [[0 for x in range(9)] for y in range(9)]

    board[0][0] = 6     # <-- set
    board[1][0] = 4
    board[2][0] = 5
    board[3][0] = 1     # <-- set
    board[4][0] = 9
    board[5][0] = 8     # <-- set
    board[6][0] = 2     # <-- set
    board[7][0] = 7
    board[8][0] = 3     # <-- set

    board[0][1] = 1
    board[1][1] = 2     # <-- set
    board[2][1] = 7
    board[3][1] = 3
    board[4][1] = 4     # <-- set
    board[5][1] = 6
    board[6][1] = 5
    board[7][1] = 9     # <-- set
    board[8][1] = 8

    board[0][2] = 8     # <-- set
    board[1][2] = 9
    board[2][2] = 3     # <-- set
    board[3][2] = 2
    board[4][2] = 7
    board[5][2] = 5     # <-- set
    board[6][2] = 4     # <-- set
    board[7][2] = 6
    board[8][2] = 1

    board[0][3] = 5     # <-- set
    board[1][3] = 1
    board[2][3] = 4     # <-- set
    board[3][3] = 6     # <-- set
    board[4][3] = 2
    board[5][3] = 7     # <-- set
    board[6][3] = 3
    board[7][3] = 8
    board[8][3] = 9     # <-- set

    board[0][4] = 2
    board[1][4] = 3     # <-- set
    board[2][4] = 8
    board[3][4] = 4
    board[4][4] = 1
    board[5][4] = 9
    board[6][4] = 6
    board[7][4] = 5     # <-- set
    board[8][4] = 7

    board[0][5] = 7     # <-- set
    board[1][5] = 6
    board[2][5] = 9
    board[3][5] = 8     # <-- set
    board[4][5] = 5
    board[5][5] = 3     # <-- set
    board[6][5] = 1     # <-- set
    board[7][5] = 4
    board[8][5] = 2     # <-- set

    board[0][6] = 4
    board[1][6] = 5
    board[2][6] = 1     # <-- set
    board[3][6] = 7     # <-- set
    board[4][6] = 8
    board[5][6] = 2
    board[6][6] = 9     # <-- set
    board[7][6] = 3
    board[8][6] = 6     # <-- set

    board[0][7] = 9
    board[1][7] = 8     # <-- set
    board[2][7] = 6
    board[3][7] = 5
    board[4][7] = 3     # <-- set
    board[5][7] = 1
    board[6][7] = 7
    board[7][7] = 2     # <-- set
    board[8][7] = 4

    board[0][8] = 3     # <-- set
    board[1][8] = 7
    board[2][8] = 2     # <-- set
    board[3][8] = 9     # <-- set
    board[4][8] = 6
    board[5][8] = 4     # <-- set
    board[6][8] = 8
    board[7][8] = 1
    board[8][8] = 5     # <-- set

    return board


def boardEqualityChecker (b1, b2):
    isSame = True
    if ( len(b1[0]) == len(b2[0])  and  len(b1[1]) == len(b2[1]) ):
        for x in range ( len(b1[0]) ):
            for y in range ( len(b1[1]) ):
                if (b1[x][y] != b2[x][y]):
                    isSame = False
    return isSame


def boardDiffChecker (b1, b2):
    diff = 0
    if ( len(b1[0]) == len(b2[0])  and  len(b1[1]) == len(b2[1]) ):
        for x in range ( len(b1[0]) ):
            for y in range ( len(b1[1]) ):
                if (b1[x][y] != b2[x][y]):
                    diff += 1
    return diff


#sudokuPrinter(exampleBoard(9, 9))
sudokuPrinter(exampleBoard2())

# Not functional test
#pSpaceSizePrinter(exampleBoard(9, 9))
