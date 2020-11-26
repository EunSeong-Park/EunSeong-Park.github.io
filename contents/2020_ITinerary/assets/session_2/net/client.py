from socket import *

ip = '127.0.0.1'
port = 10000

my_socket = socket(AF_INET, SOCK_STREAM)
my_socket.connect((ip, port))

while True:
    message = input().encode()
    my_socket.send(message)
