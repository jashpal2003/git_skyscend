import socket
c = socket.socket()
host = socket.gethostname()
print(host)
c.connect((host, 1236))

res = c.recv(1024)
print(res.decode('utf-8'))

c.close()