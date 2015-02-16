#!/usr/bin/python


import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Puerto = 1234
mySocket.bind(("localhost", Puerto))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

while True:

    print 'Waiting for connections'
    (recvSocket, address) = mySocket.accept()
    print 'HTTP request received:'
    print recvSocket.recv(1024)

    Num_Aleatorio = str(random.randint(0, 10000000))
    URL = "http://localhost:" + str(Puerto) + "/" + Num_Aleatorio
    recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                    "<html><body>Hola. <a href="
                    + Num_Aleatorio + "> Dame otra</a></p></h1>" +
                    "</body></html>" +
                    "\r\n")

    recvSocket.close()
