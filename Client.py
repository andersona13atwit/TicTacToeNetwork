import socket

host = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 1234))

s.send(b'Hello!')
    
print(s.recv(50))
s.close()