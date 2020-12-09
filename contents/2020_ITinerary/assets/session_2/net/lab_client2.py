from socket import *
from select import select
import sys
import time

HOST = '192.168.30.33'
PORT = 56789
BUFSIZE = 1024
ADDR = (HOST, PORT)

hp = 10000

clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    clientSocket.connect(ADDR)
except Exception as e:
    print("Cannot connect")
    sys.exit()
print("Connected")


while True:
    message = input("Your skill name: ")
    if not message:
        continue
    clientSocket.send(message.encode())
    msg = clientSocket.recv(1024).decode()
    print("[System]", msg)


