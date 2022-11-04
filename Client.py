import socket

"""
The Order of operations between server and client should be:

Server sends grid
Client receives
Client sends input
Server receives
Server sends turnover code / gameover code
Client makes further descisions based on such
    turnover code:
        close the connection and then 

"""




grid = [[2, 2, 2], 
        [2, 2, 2], 
        [2, 2, 2]]
def stringifyInput(incString):
    """A method to turn a byte-string version of an array into a normal string version of an array without the parentheses
        Made to be used within stringToGrid

    Args:
        incString (byte-string): A series of bytes ideally originating from the server
                                 Should be a string/byte version of an array

    Returns:
        incString: Returns the original byte-string as a normal string to be parsed by stringToGrid()
    """
    incString = incString.decode()
    incString = incString.replace('[','')
    incString = incString.replace(']', '')
    return incString

def stringToGrid(incomingString):
    """A method to turn a formatted string into a 2d array. The string must have 9 comma-spaced elements

    Args:
        incomingString (byte-string): The string to be turned into an array

    Returns:
        grid: A completed 2d array from the inputted values
    """
    incomingString = stringifyInput(incomingString)
    tempHolder = []
    grid = []
    toAppend = []
    count = 0
    arr = incomingString.split(',')
    for num in arr:
        tempHolder.append(int(num))
    for num in tempHolder:
        toAppend.append(num)
        if count < 2:
            count+=1
        else:
            grid.append(toAppend)
            count = 0
            toAppend = []
    return grid
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
        return formatInput(input('Please enter a position: '))
    symToAdd = 0 if location[0] == 'o' else 1 if location[0] == 'x' else 2
    if(len(location[1]) != 3):
        pass
    location = location[1].split(',')
    for num in range(len(location)):
        location[num] = int(location[num])
        location[num] -= 1
    return [symToAdd, location]
def addSymbol(symbol, location):
    """
    Adds symbol to grid at location\n
    Args:
        symbol (int): an integer that (if less than 2) will be added to the grid
        location (int[]): acts as coordinates in the grid and specifies where to put the symbol
    """
    if symbol < 2:
        if grid[location[0]][location[1]] == 2:
            grid[location[0]][location[1]] = symbol
        else:
            print('you entered an occupied space! Please try again')
            inputs = formatInput(input('Please enter a position: '))
            addSymbol(inputs[0], inputs[1])
    else:
        print('you entered an illegal symbol! Please try again (remember, only x and o are accepted')
        inputs = formatInput(input('Please enter a position: '))
        addSymbol(inputs[0], inputs[1])
            


host = '10.220.43.220'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 1234))

grid = stringToGrid(s.recv(50))

s.send(b'This will be an input')


s.close()