import socket
import serial
from time import sleep


def connect_to_socket():
    while True:
        try:
            s.connect((HOST, PORT))
            print("Connected to socket")
            return
        except:
            pass
        print("Failed, Retrying")
        sleep(5)


# This actually resets the arduino and restarts the stream
ser = serial.Serial('COM4', 9600)

HOST = "localhost"
PORT = 5300
TRIGGER = 5

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    connect_to_socket()
    while True:
        sensor_data = ser.readline().decode().rstrip().split(": ")
        sensor_data[1] = int(sensor_data[1]) > TRIGGER
        print(sensor_data)

        s.sendall((sensor_data[0] + ": " + str(sensor_data[1]) + "\n").encode())
