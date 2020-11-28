from socket import *

ip = '127.0.0.1'
port = 9999

my_socket = socket(AF_INET, SOCK_STREAM)
my_socket.connect((ip, port))

data = my_socket.recv(100000).decode()
open("downloaded.txt", 'w').write(data)
