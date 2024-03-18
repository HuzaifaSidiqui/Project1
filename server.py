import socket 
import threading 

PORT = 5050
SERVER = "192.168.18.16"
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "Disconnected"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected.")

    connected = True
    while connected:
        msg_length_str = conn.recv(HEADER).decode(FORMAT)
        if msg_length_str:
            try:
                msg_length = int(msg_length_str)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                print(f"[{addr}] {msg}")
            except ValueError:
                print(f"[{addr}] Invalid message length: {msg_length_str}")
                connected = False
    conn.close()

def start():
    server.listen()
    print(f"[Listening] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active connections] {threading.active_count() - 1}")

print("[Starting] Server is starting")
start()
