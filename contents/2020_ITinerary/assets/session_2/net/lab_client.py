from socket import *
from select import select
import sys
import time

HOST = '127.0.0.1'
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

s = time.time()
while True:
    #message = input("Your skill name: ")
    #if not message:
    #    continue


    if time.time() - s > 3:
        s = time.time()
        clientSocket.send("Normal".encode())
        print(clientSocket.recv(1024).decode())
        print("do")


    #clientSocket.send(message.encode())
    #msg = clientSocket.recv(1024).decode()
    #print("[System]", msg)


