# import socket

# host = ''

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((host, 1234))

# s.send(b'Hello!')
    
# print(s.recv(50))
# s.close()

initGrid = [[1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]]
def stringifyInput(incString):
    incString = incString.decode()
    incString = incString.replace('[','')
    incString = incString.replace(']', '')
    return incString
def stringToGrid(incomingString):
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
initString = bytes(str(initGrid),'utf-8')
print(stringToGrid(initString))


# print(stringToGrid(initGrid))