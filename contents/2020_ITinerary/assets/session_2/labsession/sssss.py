'''
send: Normal / Lucky
recv: some message from server

IP: 192.168.30.33
Port: 56789
'''
from socket import *

ip, port = '127.0.0.1', 56789
addr = (ip, port)

my_socket = socket(AF_INET, SOCK_STREAM)

my_socket.connect(addr)
print("Connected.")

while 1:
    my_socket.send("Normal".encode())
    print(my_socket.recv(1024).decode())


while True:
    message = input("Your skill name: ")
    if not message:
        continue
    clientSocket.send(message.encode())
    msg = clientSocket.recv(1024).decode()
    print("[System]", msg)


