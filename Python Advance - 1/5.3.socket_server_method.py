import socket

host = socket.gethostname()
port = 12342
s = socket.socket()
s.bind((host, port))

s.listen(5)

def add(x, y):
    return x + y

while True:
    conn, addr = s.accept()
    print("Connected by ", addr)
    data = conn.recv(1024)
    print(conn)
    if data:
        print("Data Received", data)
        dt = data.decode('utf-8')
        print("DT", dt)
        d = dt.split(",")
        print("Data Received string", d)
        data_add = add(int(d[0]), int(d[1]))
        conn.send(str(data_add).encode('utf-8'))
conn.close()