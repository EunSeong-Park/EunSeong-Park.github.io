from socket import *

def get_ip_port():
    # Expected input: [IP]:[PORT] / ex: 192.168.10.4:200
    addr = input("Enter your IP and address: ").split(":")
    return (addr[0], int(addr[1]))

ip, port = get_ip_port()
file = open('sample.txt', 'rb')
filedata = file.read()

my_socket = socket(AF_INET, SOCK_STREAM)
my_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

my_socket.bind((ip, port))
my_socket.listen()
c_socket, address = my_socket.accept()


c_socket.send(filedata)
