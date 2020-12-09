from socket import *
from select import *
import sys
import random
import time

HOST = ''
PORT = 56789
BUFSIZE = 1024
ADDR = (HOST, PORT)
hp = 1000000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(ADDR)

serverSocket.listen(30)
connection_list = [serverSocket]
print('[SYSTEM] Waiting...')
s = time.time()

while connection_list:
    if time.time() - s < 1:
        continue
    s = time.time()
    try:
        read_socket, write_socket, error_socket = select(connection_list, [], [], 1)

        for sock in read_socket:
            if sock == serverSocket:
                clientSocket, addr_info = serverSocket.accept()
                connection_list.append(clientSocket)
                print('[SYSTEM] New Connection (current member: ' +
                      str(len(connection_list)-1) + ")")

            else:
                try:
                    data = sock.recv(BUFSIZE)
                except ConnectionResetError:
                    connection_list.remove(sock)
                    sock.close()
                    print('[System] Client Disconnected (current member: ' +
                          str(len(connection_list)-1) + ")")
                    continue

                if data:
                    skill = data.decode()
                    msg = ""
                    damage = max(1, (len(connection_list) - 1) ** 0.5)
                    if skill == "Lucky":
                        luk = random.randint(0, 100)
                        if luk == 100:
                            hp -= int(1000 * damage)
                            msg += "SUPER-DUPER AMAZING ATTACK!"
                        if luk > 90:
                            hp -= int(100 * damage)
                            msg += "SUPER LUCKY ATTACK!"
                        elif luk > 50:
                            hp -= int(50 * damage)
                            msg += "LUCKY ATTACK!"
                        elif luk < 5:
                            msg += "SUPER UNLUCKY ATTACK... you died"
                            sock.send(msg.encode())
                            connection_list.remove(sock)
                            sock.close()
                            continue
                        else:
                            msg += "LUCKY ATTACK! but failed..."

                    elif skill == "Normal":
                        hp -= int(30 * damage)
                        msg += "NORMAL ATTACK!"
                    else:
                        msg += "Nothing happened..."
                    if hp <= 0:
                        sock.send("You win!!!".encode())
                        connection_list.remove(sock)
                        sock.close()
                        continue

                    msg += "\nCurrent HP: " + str(hp) +" / 1000000"
                    print("[SYSTEM] Current HP: " + str(hp) +" / 1000000")
                    sock.send(msg.encode())
    except KeyboardInterrupt:
        serverSocket.close()
        sys.exit()
