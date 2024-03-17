import socket

host = socket.gethostname()
port = 12342

a = input('Enter first number: ')
b = input('Enter second number: ')
c = a+','+b
print(c)

print("Sending string {0} to server" .format(c))

s = socket.socket()
s.connect((host,port))

s.send(c.encode('utf-8'))
data = s.recv(1024)
print(int(data.decode('utf-8')))

s.close()

