import socket
s=socket.socket()
s.connect(('localhost',9000))
while True:
    print(s.recv(1024).decode())
    s.send("acknoledgement recieved from the server".encode())