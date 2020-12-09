from socket import *

ip, port = '127.0.0.1', 56789

my_socket = socket(AF_INET, SOCK_STREAM)
my_socket.connect((ip, port))
print("Connected")

while True:
    message = input("Attack type: ")
    my_socket.send(message.encode())
    print(my_socket.recv(1024).decode())
