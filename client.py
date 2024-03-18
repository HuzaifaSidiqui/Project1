import socket
PORT = 5050
HEADER = 64
FORMAT= 'utf-8'
DISCONNECT_MESSAGE= "Disconnected"
SERVER= "192.168.186.1"
ADDR=(SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)