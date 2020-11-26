from socket import *

ip = '127.0.0.1'
port = 10000  # 1 to 65535

my_socket = socket(AF_INET, SOCK_STREAM)
my_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

my_socket.bind((ip, port))
my_socket.listen()
c_socket, address = my_socket.accept()

while True:
    data = c_socket.recv(1024).decode()
    print("Message:", data)

