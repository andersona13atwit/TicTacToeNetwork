grid = [[2, 2, 2], 
        [2, 2, 2], 
        [2, 2, 2]]
def checkWinVert():
    pass
def checkWinHoriz():
    pass
def checkWinDiag():
    pass
def printGrid():
    for row in grid:
        for col in row:
            if(col == 0):
                print('x', end=' ')
            elif(col == 1):
                print('o', end=' ')
            else:
                print('_', end=' ')
        print('')

gameOver = False

while(not(gameOver)):
    printGrid()
    gameOver = True
