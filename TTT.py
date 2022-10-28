'''
major ideas:
    save state (recomended by professor)
Key:
    0 = o
    1 = x
    2 = _
    10 = O
    11 = X
'''


grid = [[2, 2, 2], 
        [2, 2, 2], 
        [2, 2, 2]]

def checkWin():
    # Checks for vertical win
    for vert in grid:
        if(vert == [0, 0, 0]):
            print('O wins!')
            return -1
        if(vert == [1, 1, 1]):
            print('X wins!')
            return -1
    # Checks for horizontal win
    for col in range(3):
        if grid[0][col] == 0 and grid[1][col] == 0 and grid[2][col] == 0 :
            print('O wins!')
            return -1
    for col in range(3):
        if grid[0][col] == 1 and grid[1][col] == 1 and grid[2][col] == 1 :
            print('X wins!')
            return -1   

    #Checks for diagonal win
    if grid[0][0] == 0 and grid[1][1] == 0 and grid[2][2] == 0 :
        print('O wins!')
        return -1
    if grid[0][0] == 1 and grid[1][1] == 1 and grid[2][2] == 1 :
        print('X wins!')
        return -1

    if grid[2][0] == 0 and grid[1][1] == 0 and grid[0][2] == 0 :
        print('O wins!')
        return -1
    if grid[2][0] == 1 and grid[1][1] == 1 and grid[0][2] == 1 :
        print('X wins!')
        return -1
    
    return 0
    
    
def printGrid():
    for row in grid:
        for col in row:
            if(col == 1):
                print('x', end=' ')
            elif(col == 0):
                print('o', end=' ')
            else:
                print('-', end=' ')
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
# printGrid()
currentPlayer = 1
message = f'Player {currentPlayer}, please enter a position'
while(not(gameOver)):
    message = f'Player {currentPlayer}, please enter a position: '
    # location = input(message)
    
    currentPlayer+=1
    
    addSymbol(1,[0,0])
    addSymbol(1,[1,1])
    addSymbol(1,[2,2])
    printGrid()
    print()
    end = checkWin()
    if(end < 0):
        gameOver = True
