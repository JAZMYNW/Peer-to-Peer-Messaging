#echo-server.py
#example from https://realpython.com/python-sockets/
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #socket.AF_INET (IPv4) expects a two-tuple: (host, port)
    s.listen()#enables the server to accept connections
    conn, addr = s.accept() #creates a new socket
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)