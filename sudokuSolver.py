from sudokuPrinter import sudokuPrinter
from sudokuPrinter import pSpaceSizePrinter

from sudokuPrinter import exampleBoard
from sudokuPrinter import exampleBoard2
from sudokuPrinter import exampleBoard2Solution

from sudokuPrinter import boardEqualityChecker
from sudokuPrinter import boardDiffChecker

#import sudokuPrinter


# Generate possibility array
# Possibility eliminator
# Guesser/hypothesizer?


# pSpace[x][y] printer (print size på z per celle)
# Board Integrity Checker?


# "board" is a 2D (9x9) matrix of the sudoku board/matrix
def pSpaceGen ():
    w = 9   # board width
    l = 9   # board length
    h = 9   # NumberSpaceSize: possible index space (1-9 in regular sudoku)

    # Possibility Space. 3D array; 2D array of 1-9-1D-arrays
    pSpace = [[[0 for k in range(w)] for j in range(l)] for i in range(h)]
    #print (pSpace)  # PrePrint  -------
    for z in range (h):
        for x in range (w):
            for y in range (l):
                pSpace[x][y][z] = z + 1
    #print (pSpace)  # PostPrint -------
    return pSpace


def pSubSpaceCropper (boardValue, pSpace, w, h):
    psss = len(pSpace[2])   # Possibility Sub Space Size. Not used. Kill with fire?
    z = 0
    while  (z < len(pSpace[w][h])):
        #print ()
        #print (boardValue)
        #print (pSpace[w][h][z])
        if (pSpace[w][h][z] != boardValue):
            pSpace[w][h].pop(z)
        else:
            #print (z)
            #print (pSpace[w][h][z])
            z += 1
        #print (len(pSpace[w][h]))
    return pSpace


# Done
# Uses: pSubSpaceCropper()
def pElimStart (board, pSpace):
    w = len(board[0])
    l = len(board[1])
    for x in range (w):
        for y in range (l):
            if ( board[x][y] != 0 ):
                pSpace = pSubSpaceCropper (board[x][y], pSpace, x, y)
    #print (pSpace[0][0])
    return pSpace


# Remove number from pSubSpace
#def pSubSpaceRemover (pSubSpace, x, y, value):
def pSubSpaceRemover (pSubSpace, value):
    #pSpace[x][y].pop(value)
    #pSubSpace.remove(value)
    index = 0
    for i in range (len(pSubSpace)):
        if (pSubSpace[i] == value):
            index = i
    pSubSpace.pop(index)

    return pSubSpace
    """
    z = 0
    while (z < len(pSpace[x][y])):
        #i = len(pSpace[x][y])
    #for z in range (len(pSpace[x][y])):
        print ("x:" + str(x) + "\ty:" + str(y) + "\tz:" + str(z))
        if (pSpace[x][y][z] == value):
            pSpace[x][y].pop(z)
        z += 1
    #print (" ")
    """


def subSpaceSquareCheck (i):
    if (    i > 2 and i < 6 ):
        return 3
    elif (  i > 6 and i < 9 ):
        return 6
    else:
        return 0


def pElimSubSpaceCheck (subSpace, p):
    match = False
#    print ("\np\t: " + str(p))
    for i in range (len(subSpace)):
#        print ("sS[i]\t: " + str(subSpace[i]))
        if (subSpace[i] == p):
            match = True
#            print ("match\t: " + str(i) + "<---")
    return match


# Checks if number should be removed from the cell's pSubSpace
# need a thingy to find if element is in list
def pElimCheck (board, x, y, p, pSpace):
    #print ("pElimCheck")
    #if ( pSubSpaceCheckHorizontal() ):

    # Could be defined by board size
    pSubSpaceH = [0 for i in range(9)]
    pSubSpaceV = [0 for i in range(9)]
    pSubSpaceS = [0 for i in range(9)]

    sCoordX = subSpaceSquareCheck(x)
    sCoordY = subSpaceSquareCheck(y)

    # pSubSpaceS
    sCounter = 0
    for sX in range (3):
        for sY in range (3):
            pSubSpaceS[sCounter] = board[sX + sCoordX][sY + sCoordY]
            sCounter += 1
            #print ("pSubSpaceS : board[" + str(sX + sCoordX) + "][" + str(sY + sCoordY) + "]:\t" + str(board[sX + sCoordX][sY + sCoordY]))

    # pSubSpaceH
    for i in range (9):
        pSubSpaceH[i] = board[i][y]

    # pSubSpaceV
    for i in range (9):
        pSubSpaceV[i] = board[x][i]

#    print ()
#    print (pSubSpaceH)
#    print (pSubSpaceV)
#    print (pSubSpaceS)
#    print ("x:" + str(x) + "\ty:" + str(y) + "\tsCX:" + str(sCoordX) + "\tsCY:" + str(sCoordY))

    pSSH = False
    pSSV = False
    pSSS = False

    pSSH = pElimSubSpaceCheck (pSubSpaceH, p)
    pSSV = pElimSubSpaceCheck (pSubSpaceV, p)
    pSSS = pElimSubSpaceCheck (pSubSpaceS, p)


#    if (    pElimSubSpaceCheck (pSubSpaceH, p)
#        or  pElimSubSpaceCheck (pSubSpaceV, p)
#        or  pElimSubSpaceCheck (pSubSpaceS, p)):
    #print ("pSSH:pSSV:pSSS\t" + str(pSSH) + ":" + str(pSSV) + ":" + str(pSSS))
    if (pSSH or pSSV or pSSS):
#        print (str(p) + " <---------------------- YES")
        return True
    else:
#        print (str(p) + " <---------------------- NO")
        return False


def pSpaceToBoard (board, pSpace):
    for x in range (len(pSpace[0])):
        for y in range (len(pSpace[1])):
            if (len(pSpace[x][y]) == 1):
                board[x][y] = pSpace[x][y][0]
    return board


# Uses: pElimCheck()
def pElim (board, pSpace):
    #print ("pElim")
    done = False
    #print ("\n\npSpaceSizePrinter before pElim()")
    #pSpaceSizePrinter (pSpace)
    runs = 0
    while (done == False and runs < 1000):
        done = True
#        print ("\n--------------------------------------")
        for x in range (len(board[0])):
            for y in range (len(board[1])):

#                print ("x:y\t###################")
#                print (str(x) + ":" + str(y))
                # loop list
                z = 0
                while(z < len(pSpace[x][y])):
                    # if pSpace exists
                    #len(pSpace[x][y]) > 1
                    if (len(pSpace[x][y]) > 1):
#                        print ("---------------------------\nz\t: " + str(z))
                        # if pElimCheck
                        #pElimCheck (board, x, y, p, pSpace)
                        if ( pElimCheck(board, x, y, pSpace[x][y][z], pSpace) ):
                            # remove element from list
                            #pSpace[x][y].pop(z)
                            pSpace[x][y] = pSubSpaceRemover (pSpace[x][y], pSpace[x][y][z])
                            z = -1
                            done = False
                            board = pSpaceToBoard (board, pSpace)

#                    else:
#                        print ("No subspace")
#                    print ("pSpace[x][y]:")
#                    print (pSpace[x][y])
#                    print (str(x) + ":" + str(y))
#                    print ()
                    z += 1

#        print ("board before update")
        sudokuPrinter(board)
        board = pSpaceToBoard (board, pSpace)
#        print ("board after update")
#        sudokuPrinter(board)
        #doTheElimTests(board, x, y)
        #ifAnythingIsDone -> done = False
        runs += 1
        print ("pElimRuns : " + str(runs))
        #print ( boardEqualityChecker (  board,                      exampleBoard2Solution() ))
        #print ( boardEqualityChecker (  exampleBoard2Solution(),    exampleBoard2Solution() ))
        print ( boardDiffChecker (      board,                      exampleBoard2Solution() ))
        #print ( boardDiffChecker (      exampleBoard2Solution(),    exampleBoard2Solution() ))
        #print (done)
        #if blababla:
        #    done = False
    #print ("done")
    #print ("\n\npSpaceSizePrinter after pElim()")
    #pSpaceSizePrinter (pSpace)
#    print ()

#    print (pSpace[0][0])
#    print (pSpace[0][1])
#    print (pSpace[0][2])
#    print ()
#    print (pSpace[1][0])
#    print (pSpace[1][1])
#    print (pSpace[1][2])
#    print ()
#    print (pSpace[2][0])
#    print (pSpace[2][1])
#    print (pSpace[2][2])

    #print (pSpace)

    print ("\n\npSpaceValuePrinter()")
    sudokuPrinter(pSpaceValuePrinter(pSpace, 0))


# Returns the place in x and y, with the n-th value in z directions of a 3D list
def pSpaceValuePrinter (space, n):
    xSize = len(space[0])
    ySize = len(space[1])
    subSpace = [[0 for x in range(xSize)] for y in range(ySize)]

    for x in range (xSize):
        for y in range (ySize):
            subSpace[x][y] = space[x][y][n]
    return subSpace


#Test pElimStart
# Returns pSpace
#pElimStart (exampleBoard(9, 9), pSpaceGen())
#pElim(exampleBoard(9, 9), pElimStart (exampleBoard(9, 9), pSpaceGen()))
pElim(exampleBoard2(), pElimStart (exampleBoard2(), pSpaceGen()))




"""
# Example output

pSpaceValuePrinter()
-------------------------------------------------------
|  6  |  4  |  5  |  1  |  9  |  8  |  2  |  7  |  3  |
-------------------------------------------------------
|  1  |  2  |  7  |  3  |  4  |  6  |  5  |  9  |  8  |
-------------------------------------------------------
|  8  |  9  |  3  |  2  |  7  |  5  |  4  |  6  |  1  |
-------------------------------------------------------
|  5  |  1  |  4  |  6  |  2  |  7  |  8  |  3  |  9  |
-------------------------------------------------------
|  2  |  3  |  8  |  4  |  1  |  9  |  6  |  5  |  7  |
-------------------------------------------------------
|  7  |  6  |  9  |  8  |  5  |  3  |  1  |  4  |  2  |
-------------------------------------------------------
|  4  |  5  |  1  |  7  |  9  |  9  |  9  |  8  |  6  |
-------------------------------------------------------
|  9  |  8  |  6  |  5  |  3  |  1  |  7  |  2  |  4  |
-------------------------------------------------------
|  3  |  7  |  2  |  9  |  6  |  4  |  9  |  1  |  5  |
-------------------------------------------------------

"""







# hi
