import socket

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
f = open("out-proj.txt", "w")
while True:
    msg = csockid.recv(200)
    if len(msg) == 0:
        f.close()
        # Close the server socket
        ss.close()
        exit()
    msg = msg.decode('utf-8').rstrip("\n\r")[::-1] 
    f.write(msg + '\n')
