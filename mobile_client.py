import socket

HOST_NAME = "localhost"
PORT_NUM = 5301

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST_NAME, PORT_NUM))
    while True:
        print(s.recv(1024).decode())
