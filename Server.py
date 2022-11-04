import socket

currentPlayer = 1
grid = [[2, 2, 2], 
        [2, 2, 2], 
        [2, 2, 2]]

def checkWin():
    """Checks for three win conditions, horizontal, vertical, and diagonal 

    Returns:
        int: returns -1 if a win has been detected ANYWHERE, and a 0 if otherwise
    """
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
    """
    Formats the grid for output (should be removed before final implementation)
    """
    for row in grid:
        for col in row:
            if(col == 1):
                print('x', end=' ')
            elif(col == 0):
                print('o', end=' ')
            else:
                print('-', end=' ')
        print('')
def formatInput(stringInput):
    """Takes an input string and splits it into an int that represents a symbol and a location array of 2 ints that is 0<value<4

    Args:
        stringInput (String): A string in the format of "symbol int,int". Any deviance from this will be handled between here and addSymbol

    Returns:
        array: returns the two inputs that are needed for addSymbol, a symbol and a location
    """
    location = stringInput.split()
    if(len(location) != 2):
        print('You did not enter enough characters, please try another input')
        return formatInput(input(f'Player {(currentPlayer)}, please enter a position: '))
    symToAdd = 0 if location[0] == 'o' else 1 if location[0] == 'x' else 2
    if(len(location[1]) != 3):
        pass
    location = location[1].split(',')
    for num in range(len(location)):
        location[num] = int(location[num])
        location[num] -= 1
    return [symToAdd, location]
def addSymbol(location):
    """
    Adds symbol to grid at location\n
    Args:
        symbol (int): an integer that (if less than 2) will be added to the grid
        location (int[]): acts as coordinates in the grid and specifies where to put the symbol
    """
    if grid[location[0]][location[1]] == 2:
        grid[location[0]][location[1]] = currentPlayer-1
            
            
    

gameOver = False
printGrid()
message = f'Player {currentPlayer}, please enter a position'
print('hint: formatting for adding an o to the top left corner should look like : o 1,1')
turnCounter = 0
while(not(gameOver)):
    message = f'Player {(currentPlayer)}, please enter a position: '
    inputs = formatInput(input(message))
    addSymbol(inputs[0],inputs[1])
    currentPlayer = (currentPlayer%2)+1
    printGrid()
    print()
    end = checkWin()
    if(end < 0 or turnCounter == 8):
        print('game over!')
        gameOver = True
     
    else:
        turnCounter+=1
        print(turnCounter)


















def openSocket(addr, port):
    """A method to open a socket given a address and a port
       We need this because we are using multiple ports at a time, but we aren't worried about
       concurrence because we know what order we want the inputs to come in

    Args:
        addr (string): The address we need. While testing this will be the same in both calls, but when the time is important they will be different
        port (int): a port number which will be different between clients
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('10.220.43.220', 1234))
    s.listen(5)
    initGrid = [[1, 2, 3], 
            [4, 5, 6],
            [7, 8, 9]]

    while True:
        #connect to client
        clientsocket, address = s.accept()
        print('connected to' + address)
        
        #send client grid
        clientsocket.send(bytes(str(initGrid),'utf-8'))

        #get the valid user input for symbol location
        userInput = clientsocket.recv(50)

        #add symbol to board
        addSymbol(userInput)

        #print new board
        printGrid
        
        clientsocket.close()
        break

openSocket('10.220.43.220', 1234) #We are able to open multiple connections like this
openSocket('10.220.43.220', 1235)
