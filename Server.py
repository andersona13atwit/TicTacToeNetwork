import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(address)
    
    message = clientsocket.recv(50) + (b'Hello Client!')
    clientsocket.send(bytes(message))
    print(message)
    
    clientsocket.close()
    break

