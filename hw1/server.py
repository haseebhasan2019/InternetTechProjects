import threading
import time
import random

import socket

# def server():
try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', 50007)
ss.bind(server_binding)
ss.listen(1)
host = socket.gethostname()
print("[S]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[S]: Server IP address is {}".format(localhost_ip))
csockid, addr = ss.accept()
print ("[S]: Got a connection request from a client at {}".format(addr))

# receive message from the client.
code = "12308471"
f = open("out-proj.txt", "w")
while True:
    msg = csockid.recv(200)
    if msg == code:
        break
    msg = msg.rstrip('\n')[::-1]+'\n'
    f.write(msg)
f.close()
while True:
    msg = csockid.recv(200)
    if msg == "quit":
        # Close the server socket
        ss.close()
        exit()
    msg = msg[::-1]
    csockid.send(msg.encode('utf-8'))
