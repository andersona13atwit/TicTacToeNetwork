import socket
import time
from threading import Thread
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
            return -2
    # Checks for horizontal win
    for col in range(3):
        if grid[0][col] == 0 and grid[1][col] == 0 and grid[2][col] == 0 :
            print('O wins!')
            return -1
    for col in range(3):
        if grid[0][col] == 1 and grid[1][col] == 1 and grid[2][col] == 1 :
            print('X wins!')
            return -2 

    #Checks for diagonal win
    if grid[0][0] == 0 and grid[1][1] == 0 and grid[2][2] == 0 :
        print('O wins!')
        return -1
    if grid[0][0] == 1 and grid[1][1] == 1 and grid[2][2] == 1 :
        print('X wins!')
        return -2

    if grid[2][0] == 0 and grid[1][1] == 0 and grid[0][2] == 0 :
        print('O wins!')
        return -1
    if grid[2][0] == 1 and grid[1][1] == 1 and grid[0][2] == 1 :
        print('X wins!')
        return -2
    
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

def addSymbol(location):
    """
    Adds symbol to grid at location\n
    Args:
        location (String): acts as coordinates in the grid and specifies where to put the symbol, has to be put into array form first
    """
    if(isinstance(location, str)):
        location = location.split(',')
        
        if grid[int(location[0])][int(location[1])] == 2:
            grid[int(location[0])][int(location[1])] = currentPlayer-1
            


def openSocket(addr, port):
    """A method to open a socket given a address and a port
       We need this because we are using multiple ports at a time, but we aren't worried about
       concurrence because we know what order we want the inputs to come in

    Args:
        addr (string): The address we need. While testing this will be the same in both calls, but when the time is important they will be different
        port (int): a port number which will be different between clients
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((addr, port))
    s.listen(5)

    while True:
        #connect to client
        clientsocket, address = s.accept()
        print('connected to ' + address[0])
        
        #send client grid
        clientsocket.send(bytes(str(grid),'utf-8'))

        #get the valid user input for symbol location
        userInput = clientsocket.recv(50)

        #add symbol to board
        addSymbol(userInput.decode())

        #print new board
        printGrid()
        
        clientsocket.close()
        break

def gameEndSocket(addr, port):
    """A method to open a socket given a address and a port
       The socket that sends game over and ends the game

    Args:
        addr (string): The address we need. While testing this will be the same in both calls, but when the time is important they will be different
        port (int): a port number which will be different between clients
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((addr, port))
    s.listen(5)

    while True:
        #connect to client
        clientsocket, address = s.accept()
        print('connected to ' + address)

        #Check for tie
        if turnCounter == 8:
            clientsocket.send(bytes('Tie!','utf-8'))

        #Check for winner
        if checkWin == -1:
            clientsocket.send(bytes('O wins!','utf-8'))
        else:
            clientsocket.send(bytes('X wins!','utf-8'))
        
        #send client grid
        clientsocket.send(bytes(str(grid),'utf-8'))

        #print final board
        printGrid()
        
        clientsocket.close()
        break

currentPort = 1234
turnCounter = 0

while True:

    port = 1234

    #Get input from players
    openSocket('10.12.60.138', currentPort) #We are able to open multiple connections like this

    if checkWin() < 0 or turnCounter == 8:
        #Give the player game over
        gameEndSocket('10.12.60.138', currentPort)

        #Change port
        if currentPort == 1234:
            currentPort =+ 1
        else:
            currentPort =- 1

        turnCounter =+ 1

        #Give the other player game over
        gameEndSocket('10.12.60.138', currentPort)
        break

    #Change port
    if currentPort == 1234:
        currentPort =+ 1
    else:
        currentPort =- 1

    turnCounter =+ 1


    
