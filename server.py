import socket
from time import sleep

ARDUINO_PORT_NUM = 5300
MOBILE_PORT_NUM = 5301
NUM_SENSORS = 2
HOST_NAME = 'localhost'

is_free = [False] * NUM_SENSORS  # >= 0 means free, < means taken


def connect_to_mobile_socket():
    try:
        mobile_client_socket.connect((HOST_NAME, MOBILE_PORT_NUM))
        print('Connected to mobile socket')
    except:
        print("Connection failed")
        pass


arduino_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
arduino_client_socket.bind((HOST_NAME, ARDUINO_PORT_NUM))
arduino_client_socket.listen()

mobile_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mobile_client_socket.bind((HOST_NAME, MOBILE_PORT_NUM))
mobile_client_socket.listen()

a_soc, a_address = arduino_client_socket.accept()
m_soc, m_address = mobile_client_socket.accept()

i = 0
while True:

    vals = a_soc.recv(1024).decode().rstrip().split(": ")
    # print(vals)
    index = int(vals[0])
    status = vals[1] == 'True'

    # m_soc.send(b"HTTP/1.1 200 OK\r\nConnection: upgrade \r\n\r\n")
    # m_soc.send(b"i\r\n")
    # sleep(1)

    if is_free[index] != status:
        print(vals)
        m_soc.sendall((':'.join(vals) + "\r\n").encode())
        # m_soc.send(b"HTTP/1.1 200 OK\r\n\r\n")
        is_free[index] = status

