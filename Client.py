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
def stringToGrid(incomingString):
    arr1 = incomingString[0:6].split(',')
    arr2 = incomingString[6:12].split(',')
    arr2.pop(len(arr2)-1)
    arr3 = incomingString[12:17].split(',')
    arr1.pop(len(arr1)-1)
    grid = [arr1, arr2, arr3]
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] = int(grid[x][y])
    return grid

print(bytes(str(initGrid),'utf-8'))
# print(stringToGrid(initGrid))