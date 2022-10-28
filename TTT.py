'''
Key:
    0 = o
    1 = x
    2 = _
    10 = O
    11 = X
'''

from tabnanny import check


grid = [[2, 2, 2], 
        [2, 2, 2], 
        [2, 2, 2]]

def checkWinVert():
    xSum = 0
    oSum = 0
    for y in range(len(grid)):
        if(grid[y][0] == 1):
            oSum+=1
    if oSum == len(grid):
        return 1
    else:
        for x in range(len(grid)):
            if(grid[x][0] == 0):
                xSum+=1
        if(xSum == len(grid)):
            return 0
    

def checkWinHoriz():
    xSum = 0
    oSum = 0
    for y in range(len(grid)):
        for z in range(len(grid[y])):
            if(grid[y][z] == 1):
                oSum+=1
    if oSum == len(grid):
        return 1
    
    
    else:
        for x in range(len(grid)):
            if(grid[x][0] == 0):
                xSum+=1
        if(xSum == len(grid)):
            return 0

def checkWinDiag():
    return True

def checkWin():
    vertWin = checkWinVert()
    horizWin = checkWinHoriz()
    diagWin = checkWinDiag()
    if(vertWin == 1):
        print('X wins!')
        return -1
    if(horizWin == 1):
        print('X wins!')
        return -1
    if(diagWin == 1):
        print('X wins!')
        return -1
    
    if(vertWin == 0):
        print('O wins!')
        return -1
    if(horizWin == 0):
        print('O wins!')
        return -1
    if(diagWin == 0):
        print('O wins!')
        return -1
    return 0
    
    
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

def addSymbol(symbol, location):
    """
    Adds symbol to grid at location\n
    Args:
        symbol (int): an integer that (if less than 2) will be added to the grid
        location (int[]): acts as coordinates in the grid and specifies where to put the symbol
    """
    if(symbol < 2):
        grid[location[0]][location[1]] = symbol
    
    

gameOver = False
printGrid()
currentPlayer = 1
message = f'Player {currentPlayer}, please enter a position'
while(not(gameOver)):
    message = f'Player {currentPlayer}, please enter a position: '
    location = input(message)
    
    currentPlayer+=1
    
    addSymbol(0, [0,0])
    addSymbol(0, [1,0])
    addSymbol(0, [2,0])
    printGrid()
    print()
    end = checkWin()
    if(end < 0):
        gameOver = True
