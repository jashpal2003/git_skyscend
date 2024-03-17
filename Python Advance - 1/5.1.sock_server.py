import socket

s = socket.socket()
print(s)

host = socket.gethostname()
print("HOST",host)

s.bind((host, 1236))

s.listen(5)
help(s.listen)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    print(c)
    c.send('Thank you for connecting'.encode('utf-8'))
s.close()