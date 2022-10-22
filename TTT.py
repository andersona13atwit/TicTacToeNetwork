'''
Key:
    0 = o
    1 = x
    2 = _
    10 = O
    11 = X
'''

from audioop import add


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
    message = f'Player {currentPlayer}, please enter a position'
    print(message)
    currentPlayer+=1
    
    addSymbol(1, [0,0])
    printGrid()
    
    gameOver = True
